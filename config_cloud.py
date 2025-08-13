# SPDX-FileCopyrightText: 2024 MoonlightByte
# SPDX-License-Identifier: Fair-Source-1.0
# License: See LICENSE file in the repository root

"""
Cloud Configuration for NeverEndingQuest
Configuração específica para deploy em plataformas cloud (Railway, Render, etc.)
"""

import os
from model_config import *

# --- Cloud Environment Configuration ---
# Usar variáveis de ambiente para segurança
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyApY_Y_nhZN4AAPj7_Den0f9YcCi45wuno')
OPENAI_API_KEY = os.getenv('GEMINI_API_KEY', 'AIzaSyApY_Y_nhZN4AAPj7_Den0f9YcCi45wuno')  # Backward compatibility

# --- Web Server Configuration ---
# Cloud platforms use PORT environment variable
WEB_PORT = int(os.getenv('PORT', 8357))
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
HOST = os.getenv('HOST', '0.0.0.0')  # Bind to all interfaces for cloud

# --- Database Configuration ---
# Use PostgreSQL if available, fallback to SQLite
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///neverending_quest.db')

# --- File Storage Configuration ---
# Cloud storage options
USE_CLOUD_STORAGE = os.getenv('USE_CLOUD_STORAGE', 'False').lower() == 'true'
GOOGLE_DRIVE_CREDENTIALS = os.getenv('GOOGLE_DRIVE_CREDENTIALS', None)

# --- Module Configuration ---
MODULES_DIR = os.getenv('MODULES_DIR', 'modules')
DEFAULT_MODULE = os.getenv('DEFAULT_MODULE', 'The_Thornwood_Watch')

# --- Session Configuration ---
# Use Redis for distributed sessions if available
REDIS_URL = os.getenv('REDIS_URL', None)
SESSION_TYPE = 'redis' if REDIS_URL else 'filesystem'

# --- Security Configuration ---
SECRET_KEY = os.getenv('SECRET_KEY', 'dungeon-master-secret-key-change-in-production')

# --- Logging Configuration ---
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
SENTRY_DSN = os.getenv('SENTRY_DSN', None)  # Error tracking

# --- Performance Configuration ---
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max upload
UPLOAD_TIMEOUT = 30  # seconds

print(f"[CONFIG] Cloud configuration loaded")
print(f"[CONFIG] Port: {WEB_PORT}")
print(f"[CONFIG] Debug: {DEBUG}")
print(f"[CONFIG] Database: {'PostgreSQL' if 'postgresql' in DATABASE_URL else 'SQLite'}")
print(f"[CONFIG] Cloud Storage: {USE_CLOUD_STORAGE}")
