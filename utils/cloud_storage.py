# SPDX-FileCopyrightText: 2024 MoonlightByte
# SPDX-License-Identifier: Fair-Source-1.0
# License: See LICENSE file in the repository root

"""
Cloud Storage Manager for NeverEndingQuest using Google Drive API
Handles authentication, file uploads, downloads, and synchronization.
"""

import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_PICKLE_FILE = 'token.pickle'

class DriveManager:
    def __init__(self):
        """Initializes the DriveManager and authenticates the user."""
        self.service = self._get_drive_service()

    def _get_drive_service(self):
        """
        Gets an authorized Google Drive service object.
        Uses environment variables in production and local files for development.
        """
        creds = None
        
        # --- Production Environment: Use environment variables ---
        if 'GOOGLE_CREDENTIALS_JSON' in os.environ and 'GOOGLE_TOKEN_JSON' in os.environ:
            creds_data = json.loads(os.environ['GOOGLE_CREDENTIALS_JSON'])['installed']
            token_data = json.loads(os.environ['GOOGLE_TOKEN_JSON'])

            creds = Credentials(
                token=token_data.get('token'),
                refresh_token=token_data.get('refresh_token'),
                token_uri=creds_data.get('token_uri'),
                client_id=creds_data.get('client_id'),
                client_secret=creds_data.get('client_secret'),
                scopes=SCOPES
            )

        # --- Development Environment: Use local files ---
        else:
            if os.path.exists(TOKEN_PICKLE_FILE):
                with open(TOKEN_PICKLE_FILE, 'rb') as token:
                    creds = pickle.load(token)
        
        # If credentials are not valid, refresh or run the local auth flow
        if not creds or not creds.valid:
            # Check if token is expired and can be refreshed
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                    # If in dev, save the refreshed token
                    if 'GOOGLE_CREDENTIALS_JSON' not in os.environ:
                        with open(TOKEN_PICKLE_FILE, 'wb') as token:
                            pickle.dump(creds, token)
                except Exception as e:
                    print(f"[WARNING] Could not refresh token: {e}. Re-authentication will be required.")
                    creds = None # Force re-authentication
            
            # If no valid creds after trying to refresh, run the one-time setup flow (local only)
            if not creds:
                if not os.path.exists(CREDENTIALS_FILE):
                    print(f"[ERROR] Credentials file '{CREDENTIALS_FILE}' not found.")
                    print("Please download it from Google Cloud Console and place it in the root directory.")
                    return None
                
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            
                # Save the fresh token for the next run in development
                with open(TOKEN_PICKLE_FILE, 'wb') as token:
                    pickle.dump(creds, token)

        if not creds:
            print("[ERROR] Failed to authenticate with Google Drive.")
            return None

        return build('drive', 'v3', credentials=creds)

    def find_folder_id(self, folder_name, parent_id=None):
        """Finds the ID of a folder by name. Returns None if not found."""
        query = f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
        if parent_id:
            query += f" and '{parent_id}' in parents"
        else:
            query += " and 'root' in parents"

        response = self.service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
        for file in response.get('files', []):
            return file.get('id')
        return None

    def create_folder(self, folder_name, parent_id=None):
        """Creates a folder and returns its ID."""
        existing_folder_id = self.find_folder_id(folder_name, parent_id)
        if existing_folder_id:
            return existing_folder_id

        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        if parent_id:
            file_metadata['parents'] = [parent_id]
        
        folder = self.service.files().create(body=file_metadata, fields='id').execute()
        print(f"[Cloud Storage] Created folder '{folder_name}' with ID: {folder.get('id')}")
        return folder.get('id')

    def upload_file(self, local_path, cloud_folder_id):
        """Uploads a file to a specific folder in Google Drive."""
        file_name = os.path.basename(local_path)
        media = MediaFileUpload(local_path, resumable=True)
        
        # Check if file already exists
        query = f"name = '{file_name}' and '{cloud_folder_id}' in parents and trashed = false"
        response = self.service.files().list(q=query, spaces='drive', fields='files(id)').execute()
        files = response.get('files', [])
        
        file_metadata = {'name': file_name, 'parents': [cloud_folder_id]}

        if files:
            # Update existing file
            file_id = files[0].get('id')
            request = self.service.files().update(fileId=file_id, body=file_metadata, media_body=media)
            print(f"[Cloud Storage] Updating '{file_name}' in Drive...")
        else:
            # Create new file
            request = self.service.files().create(body=file_metadata, media_body=media, fields='id')
            print(f"[Cloud Storage] Uploading '{file_name}' to Drive...")
        
        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                print(f"Uploaded {int(status.progress() * 100)}%")
        print(f"[Cloud Storage] Upload complete for '{file_name}'.")

    def download_file(self, file_name, cloud_folder_id, local_path):
        """Downloads a file from Google Drive."""
        query = f"name = '{file_name}' and '{cloud_folder_id}' in parents and trashed = false"
        response = self.service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
        files = response.get('files', [])

        if not files:
            print(f"[Cloud Storage] File '{file_name}' not found in Drive.")
            return False

        file_id = files[0].get('id')
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")

        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        with open(local_path, 'wb') as f:
            f.write(fh.getvalue())
        print(f"[Cloud Storage] Downloaded '{file_name}' to '{local_path}'.")
        return True

# Example Usage:
if __name__ == '__main__':
    drive = DriveManager()
    if drive.service:
        # 1. Create a main folder for the game
        game_folder_id = drive.create_folder('NeverEndingQuest_Saves')

        # 2. Create a subfolder for characters
        characters_folder_id = drive.create_folder('characters', parent_id=game_folder_id)

        # 3. Example: Upload a character file
        # Create a dummy file for testing
        with open('test_character.json', 'w') as f:
            f.write('{"name": "Test Character"}')
        drive.upload_file('test_character.json', characters_folder_id)
        os.remove('test_character.json')

        # 4. Example: Download a character file
        drive.download_file('test_character.json', characters_folder_id, 'downloaded_character.json')
