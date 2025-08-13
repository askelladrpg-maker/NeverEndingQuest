# SPDX-FileCopyrightText: 2024 MoonlightByte
# SPDX-License-Identifier: Fair-Source-1.0
# License: See LICENSE file in the repository root
# This software is subject to the terms of the Fair Source License.

import os
from model_config import *

# --- API Configuration ---
# This configuration reads the API key from an environment variable, which is the
# secure best practice for production deployments. For local development, it falls
# back to a hardcoded key if the environment variable is not set.

# In your hosting service (like Render), set an environment variable named 'GEMINI_API_KEY'
# with your actual key.
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyApY_Y_nhZN4AAPj7_Den0f9YcCi45wuno")

# Legacy OpenAI key for backward compatibility. It uses the same environment variable.
OPENAI_API_KEY = GEMINI_API_KEY

# --- Module folder structure ---
MODULES_DIR = "modules"
DEFAULT_MODULE = "The_Thornwood_Watch"

# --- Web Interface Configuration ---
# The port is read from the PORT environment variable, which is standard for most hosting providers.
# It defaults to 8357 for local development.
WEB_PORT = int(os.environ.get('PORT', 8357))