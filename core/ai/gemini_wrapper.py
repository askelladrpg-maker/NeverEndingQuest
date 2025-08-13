#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 MoonlightByte
# SPDX-License-Identifier: Fair-Source-1.0
# License: See LICENSE file in the repository root
# This software is subject to the terms of the Fair Source License.

# ============================================================================
# GEMINI_WRAPPER.PY - GEMINI API COMPATIBILITY LAYER
# ============================================================================
# 
# ARCHITECTURE ROLE: AI Integration Abstraction Layer for Gemini API
# 
# This module provides a compatibility wrapper that mimics OpenAI's interface
# but uses Google's Gemini API underneath. This allows for seamless migration
# from OpenAI to Gemini with minimal code changes.
# 
# KEY RESPONSIBILITIES:
# - Provide OpenAI-compatible interface for Gemini API
# - Handle response format conversion between APIs
# - Manage Gemini client instances and configurations
# - Implement error handling and retry logic
# - Support usage tracking for Gemini API calls
# 
# COMPATIBILITY FEATURES:
# - Mimics OpenAI client.chat.completions.create() interface
# - Converts Gemini responses to OpenAI-compatible format
# - Supports temperature, max_tokens, and other parameters
# - Maintains conversation history format compatibility
# 
# ARCHITECTURAL INTEGRATION:
# - Drop-in replacement for OpenAI client instances
# - Maintains existing conversation flow and response parsing
# - Supports existing validation and error handling systems
# - Compatible with current usage tracking infrastructure
# ============================================================================

import google.generativeai as genai
import json
import time
from typing import Dict, List, Any, Optional
from dataclasses import dataclass


@dataclass
class GeminiUsage:
    """Mimics OpenAI usage structure for compatibility"""
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0


class GeminiMessage:
    """Mimics OpenAI message structure for compatibility"""
    def __init__(self, role: str = "assistant", content: str = ""):
        self.role = role
        self.content = content

@dataclass
class GeminiChoice:
    """Mimics OpenAI choice structure for compatibility"""
    message: GeminiMessage = None
    finish_reason: str = "stop"
    
    def __post_init__(self):
        if self.message is None:
            self.message = GeminiMessage()


@dataclass
class GeminiResponse:
    """Mimics OpenAI response structure for compatibility"""
    id: str = ""
    object: str = "chat.completion"
    created: int = 0
    model: str = ""
    choices: List[GeminiChoice] = None
    usage: GeminiUsage = None
    
    def __post_init__(self):
        if self.choices is None:
            self.choices = [GeminiChoice()]
        if self.usage is None:
            self.usage = GeminiUsage()
        if self.created == 0:
            self.created = int(time.time())


class GeminiChatCompletions:
    """Mimics OpenAI chat.completions interface"""
    
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        
    def create(self, model: str, messages: List[Dict], temperature: float = 0.7, 
               max_tokens: Optional[int] = None, **kwargs) -> GeminiResponse:
        """
        Create a chat completion using Gemini API with OpenAI-compatible interface
        
        Args:
            model: Gemini model name (e.g., "gemini-1.5-pro")
            messages: List of message dictionaries with 'role' and 'content'
            temperature: Sampling temperature (0.0 to 1.0)
            max_tokens: Maximum tokens to generate
            **kwargs: Additional parameters (ignored for compatibility)
            
        Returns:
            GeminiResponse object compatible with OpenAI response format
        """
        try:
            # Initialize Gemini model
            gemini_model = genai.GenerativeModel(model)
            
            # Convert OpenAI messages to Gemini format
            gemini_prompt = self._convert_messages_to_prompt(messages)
            
            # Configure generation parameters
            generation_config = genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens if max_tokens else 8192,
            )
            
            # Generate response
            response = gemini_model.generate_content(
                gemini_prompt,
                generation_config=generation_config
            )
            
            # Convert Gemini response to OpenAI format
            return self._convert_response_to_openai_format(response, model)
            
        except Exception as e:
            # Return error response in OpenAI format
            error_response = GeminiResponse(
                model=model,
                choices=[GeminiChoice(message={"role": "assistant", "content": f"Error: {str(e)}"})],
                usage=GeminiUsage()
            )
            return error_response
    
    def _convert_messages_to_prompt(self, messages: List[Dict]) -> str:
        """Convert OpenAI message format to Gemini prompt format"""
        prompt_parts = []
        
        for message in messages:
            role = message.get("role", "")
            content = message.get("content", "")
            
            if role == "system":
                prompt_parts.append(f"System: {content}")
            elif role == "user":
                prompt_parts.append(f"User: {content}")
            elif role == "assistant":
                prompt_parts.append(f"Assistant: {content}")
            else:
                prompt_parts.append(content)
        
        return "\n\n".join(prompt_parts)
    
    def _clean_json_response(self, content: str) -> str:
        """Clean Gemini response to remove markdown code blocks"""
        import re
        # Remove markdown code blocks (```json and ```)
        content = re.sub(r'```json\s*', '', content)
        content = re.sub(r'```\s*$', '', content)
        content = content.strip()
        return content
    
    def _convert_response_to_openai_format(self, gemini_response, model: str) -> GeminiResponse:
        """Convert Gemini response to OpenAI-compatible format"""
        try:
            raw_content = gemini_response.text if hasattr(gemini_response, 'text') else ""
            # Clean JSON response to remove markdown code blocks
            content = self._clean_json_response(raw_content)
            
            # Estimate token usage (Gemini doesn't provide exact counts like OpenAI)
            prompt_tokens = len(content.split()) * 1.3  # Rough estimation
            completion_tokens = len(content.split())
            total_tokens = int(prompt_tokens + completion_tokens)
            
            return GeminiResponse(
                id=f"gemini-{int(time.time())}",
                model=model,
                choices=[GeminiChoice(
                    message=GeminiMessage(role="assistant", content=content),
                    finish_reason="stop"
                )],
                usage=GeminiUsage(
                    prompt_tokens=int(prompt_tokens),
                    completion_tokens=completion_tokens,
                    total_tokens=total_tokens
                )
            )
            
        except Exception as e:
            return GeminiResponse(
                model=model,
                choices=[GeminiChoice(message=GeminiMessage(role="assistant", content=f"Response conversion error: {str(e)}"))],
                usage=GeminiUsage()
            )


class GeminiChat:
    """Mimics OpenAI chat interface"""
    
    def __init__(self, api_key: str):
        self.completions = GeminiChatCompletions(api_key)


class GeminiClient:
    """
    Gemini client that mimics OpenAI client interface for compatibility
    
    This class provides a drop-in replacement for OpenAI client instances,
    allowing existing code to work with minimal changes.
    """
    
    def __init__(self, api_key: str):
        """
        Initialize Gemini client with API key
        
        Args:
            api_key: Google Gemini API key
        """
        self.api_key = api_key
        self.chat = GeminiChat(api_key)
        
    def __repr__(self):
        return f"GeminiClient(api_key='***')"


# Compatibility function for easy migration
def OpenAI(api_key: str) -> GeminiClient:
    """
    Drop-in replacement for OpenAI client initialization
    
    Usage:
        # Old: client = OpenAI(api_key=OPENAI_API_KEY)
        # New: client = OpenAI(api_key=GEMINI_API_KEY)  # Uses Gemini underneath
        
    Args:
        api_key: Gemini API key
        
    Returns:
        GeminiClient instance with OpenAI-compatible interface
    """
    return GeminiClient(api_key)
