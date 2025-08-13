#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 MoonlightByte
# SPDX-License-Identifier: Fair-Source-1.0
# License: See LICENSE file in the repository root
# This software is subject to the terms of the Fair Source License.

"""
AI-powered initiative tracker that analyzes combat conversation to determine who has acted.
Used to enhance the combat state display with live turn tracking.
"""

import json
import re
from core.ai.gemini_wrapper import OpenAI
from config import GEMINI_API_KEY, DM_MAIN_MODEL
import logging

logger = logging.getLogger(__name__)

def extract_recent_combat_messages(conversation, current_round):
    """Extract messages relevant to the current and previous round."""
    # Filter out system messages
    non_system_messages = [msg for msg in conversation if msg["role"] != "system"]
    
    # Look for round markers
    round_markers = []
    for i, msg in enumerate(conversation):
        if msg["role"] == "system":
            continue
            
        content = msg["content"]
        
        # Look for round markers in user messages (combat state)
        if msg["role"] == "user" and "Round:" in content:
            match = re.search(r"Round:\s*(\d+)", content)
            if match:
                round_num = int(match.group(1))
                round_markers.append({"index": i, "round": round_num})
        
        # Look for round markers in assistant messages
        elif msg["role"] == "assistant":
            json_match = re.search(r'"combat_round"\s*:\s*(\d+)', content)
            if json_match:
                round_num = int(json_match.group(1))
                round_markers.append({"index": i, "round": round_num})
    
    # Find messages for current and previous round
    previous_round = current_round - 1 if current_round > 1 else 1
    start_idx = 0
    
    # Find the start of the previous round
    for marker in round_markers:
        if marker["round"] == previous_round:
            start_idx = marker["index"]
            break
    
    # Extract relevant messages
    relevant_messages = []
    for i in range(start_idx, len(conversation)):
        if conversation[i]["role"] != "system":
            relevant_messages.append(conversation[i])
    
    return relevant_messages[-20:]  # Limit to last 20 messages to stay within token limits

def create_initiative_prompt(messages, creatures, current_round):
    """Create prompt for AI to analyze initiative."""
    # Format initiative order
    initiative_order = []
    for creature in sorted(creatures, key=lambda x: x.get("initiative", 0), reverse=True):
        name = creature.get("name", "Unknown")
        init_value = creature.get("initiative", 0)
        status = creature.get("status", "alive")
        initiative_order.append(f"{name} ({init_value}) - {status}")
    
    # Format conversation
    conversation_text = ""
    for msg in messages:
        role = "Player" if msg["role"] == "user" else "DM"
        conversation_text += f"\n{role}: {msg['content']}\n"
    
    # Debug logging
    logger.debug(f"Initiative AI analyzing Round {current_round}")
    logger.debug(f"Number of messages: {len(messages)}")
    if messages:
        logger.debug(f"Last message role: {messages[-1]['role']}")
        logger.debug(f"Last message preview: {messages[-1]['content'][:200]}...")
    
    prompt = f"""You are analyzing combat in Round {current_round}. Your ONLY job is to determine who has acted and who hasn't acted yet in THIS SPECIFIC ROUND.

CURRENT ROUND: {current_round}

INITIATIVE ORDER:
{chr(10).join(initiative_order)}

RECENT COMBAT CONVERSATION:
{conversation_text}

Based on the conversation above, create a **Live Initiative Tracker** showing who has acted in Round {current_round}:

**Live Initiative Tracker:**
- [X] CreatureName (Initiative) - Acted
- [>] **CurrentCreature (Initiative) - CURRENT TURN**
- [ ] NextCreature (Initiative) - Waiting
- [D] DeadCreature (Initiative) - Dead
- [S] StunnedCreature (Initiative) - Skipped (Stunned)
- [P] ParalyzedCreature (Initiative) - Skipped (Paralyzed)
- [U] UnconsciousCreature (Initiative) - Skipped (Unconscious)
- [-] OtherCondition (Initiative) - Skipped (Condition Name)

IMPORTANT INSTRUCTIONS:
1. List ALL creatures from the initiative order above (highest to lowest)
2. Use [X] followed by "Acted" for creatures who have ALREADY ACTED in Round {current_round}
3. Use [>] and bold followed by "CURRENT TURN" for the creature whose turn it is RIGHT NOW
4. Use [ ] followed by "Waiting" for creatures who HAVE NOT ACTED YET in Round {current_round}
5. Use [D] followed by "Dead" for creatures that are dead (0 HP and failed death saves)
6. Use [S] followed by "Skipped (Stunned)" for stunned creatures who couldn't act
7. Use [P] followed by "Skipped (Paralyzed)" for paralyzed creatures who couldn't act
8. Use [U] followed by "Skipped (Unconscious)" for unconscious creatures (0 HP but not dead)
9. Use [-] followed by "Skipped (Condition)" for any other condition preventing action (incapacitated, petrified, etc.)
10. DO NOT determine the round number - it is Round {current_round}
11. ONLY look at actions taken in Round {current_round}, ignore previous rounds
12. Always include the status description after the name and initiative
13. If a creature was skipped due to a condition, show the condition that caused the skip"""
    
    return prompt

def generate_live_initiative_tracker(encounter_data, conversation_history, current_round=None):
    """
    Generate a live initiative tracker showing who has acted in the current round.
    
    Args:
        encounter_data: The encounter data with creatures list
        conversation_history: Recent combat conversation messages
        current_round: The current combat round (optional, will use encounter data if not provided)
    
    Returns:
        str: Formatted initiative tracker or None if generation fails
    """
    try:
        if not GEMINI_API_KEY:
            logger.warning("OpenAI API key not configured, cannot generate initiative tracker")
            return None
        
        # Get current round
        if current_round is None:
            current_round = encounter_data.get("current_round", encounter_data.get("combat_round", 1))
        
        # Get creatures from encounter
        creatures = encounter_data.get("creatures", [])
        if not creatures:
            logger.warning("No creatures found in encounter data")
            return None
        
        # Extract relevant messages
        relevant_messages = extract_recent_combat_messages(conversation_history, current_round)
        if not relevant_messages:
            logger.warning("No relevant combat messages found")
            return None
        
        # Create prompt
        prompt = create_initiative_prompt(relevant_messages, creatures, current_round)
        
        # Query AI model
        client = OpenAI(api_key=GEMINI_API_KEY)
        response = client.chat.completions.create(
            model=DM_MAIN_MODEL,
            messages=[
                {"role": "system", "content": "You are an initiative tracker. Your ONLY job is to identify who has acted and who hasn't in the specified round. Format your response EXACTLY as requested with the Live Initiative Tracker format using [X], [>], [ ], [D], [S], [P], [U], and [-] markers for different creature states. Do not provide any other information."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1
        )
        
        # Extract the tracker from response
        tracker_text = response.choices[0].message.content
        
        # Validate that we got a properly formatted tracker
        if "**Live Initiative Tracker:**" in tracker_text:
            # Extract just the tracker portion
            tracker_start = tracker_text.find("**Live Initiative Tracker:**")
            tracker = tracker_text[tracker_start:]
            
            # Clean up any extra text after the tracker
            lines = tracker.split('\n')
            cleaned_lines = []
            valid_markers = ['[X]', '[>]', '[ ]', '[D]', '[S]', '[P]', '[U]', '[-]']
            
            for line in lines:
                if line.strip() and (
                    line.strip().startswith('**Live Initiative Tracker:**') or
                    any(line.strip().startswith(f'- {marker}') for marker in valid_markers)
                ):
                    cleaned_lines.append(line)
                elif cleaned_lines and not line.strip():
                    # Keep empty lines within the tracker
                    cleaned_lines.append(line)
                elif cleaned_lines and not any(line.strip().startswith(f'- {marker}') for marker in valid_markers):
                    # Stop if we hit non-tracker content
                    break
            
            return '\n'.join(cleaned_lines)
        else:
            logger.warning("AI response did not contain properly formatted tracker")
            return None
            
    except Exception as e:
        logger.error(f"Error generating live initiative tracker: {e}")
        return None

def format_fallback_initiative(creatures, current_round):
    """
    Create a fallback initiative display if AI generation fails.
    
    Args:
        creatures: List of creatures from encounter data
        current_round: Current combat round
        
    Returns:
        str: Formatted initiative order
    """
    lines = [f"Round: {current_round}", "Initiative Order:"]
    
    # Sort by initiative
    sorted_creatures = sorted(creatures, key=lambda x: x.get("initiative", 0), reverse=True)
    
    # Format each creature
    creature_strs = []
    for creature in sorted_creatures:
        name = creature.get("name", "Unknown")
        init = creature.get("initiative", 0)
        status = creature.get("status", "alive")
        creature_strs.append(f"{name} ({init}, {status})")
    
    lines.append(" -> ".join(creature_strs))
    return "\n".join(lines)