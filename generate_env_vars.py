# SPDX-FileCopyrightText: 2024 MoonlightByte
# SPDX-License-Identifier: Fair-Source-1.0
#
# generate_env_vars.py - Helper script to generate environment variables for deployment.
#
# Run this script LOCALLY ONE TIME to generate the necessary JSON strings for your
# Google Drive API credentials. Copy the output and add it to your hosting provider's
# environment variables.

import os
import json
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_PICKLE_FILE = 'token.pickle'

def generate_env_vars():
    """Generates the JSON strings for Google API environment variables."""
    creds = None

    # --- Step 1: Authenticate locally to generate token.pickle ---
    if os.path.exists(TOKEN_PICKLE_FILE):
        with open(TOKEN_PICKLE_FILE, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"[ERROR] '{CREDENTIALS_FILE}' not found.")
                print("Please download your Google API credentials and save them as 'credentials.json' in this directory.")
                return
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(TOKEN_PICKLE_FILE, 'wb') as token:
            pickle.dump(creds, token)

    print("\n✅ Local authentication successful. `token.pickle` is ready.")

    # --- Step 2: Read the credential files and convert to JSON ---
    if not os.path.exists(CREDENTIALS_FILE):
        print(f"[ERROR] Could not find '{CREDENTIALS_FILE}' after authentication.")
        return

    # Read credentials.json
    with open(CREDENTIALS_FILE, 'r') as f:
        credentials_json = json.load(f)
    
    # Convert the token object to a JSON string
    token_json_str = creds.to_json()

    print("\n" + "="*80)
    print("COPY THE FOLLOWING VALUES INTO YOUR HOSTING ENVIRONMENT VARIABLES:")
    print("="*80 + "\n")

    print("Variable Name: GOOGLE_CREDENTIALS_JSON")
    print("Variable Value:")
    print(json.dumps(credentials_json))
    print("-"*80 + "\n")

    print("Variable Name: GOOGLE_TOKEN_JSON")
    print("Variable Value:")
    print(token_json_str)
    print("\n" + "="*80)
    print("\nDeployment is ready!")

if __name__ == '__main__':
    generate_env_vars()
