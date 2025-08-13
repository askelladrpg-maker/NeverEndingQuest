#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 MoonlightByte
# SPDX-License-Identifier: Fair-Source-1.0

"""
Cloud Save Game Manager
Orchestrates local save operations and synchronizes them with Google Drive.
"""

import os
import shutil
from updates.save_game_manager import SaveGameManager
from utils.cloud_storage import DriveManager

class CloudSaveGameManager:
    def __init__(self, drive_manager: DriveManager):
        """Initializes the CloudSaveGameManager.

        Args:
            drive_manager: An authenticated instance of DriveManager.
        """
        self.local_manager = SaveGameManager()
        self.drive_manager = drive_manager
        self.cloud_folder_id = self.drive_manager.create_folder('NeverEndingQuest_Saves')

    def create_save_game(self, description, save_mode):
        """Creates a local save and then uploads it to the cloud."""
        # 1. Create the local save game first
        success, message = self.local_manager.create_save_game(description, save_mode)
        if not success:
            return False, message

        # `message` contains the path to the created save folder
        save_folder_path = message
        save_name = os.path.basename(save_folder_path)
        zip_path = os.path.join(self.local_manager.base_dir, f"{save_name}.zip")

        print(f"[CloudSave] Zipping save folder: {save_folder_path}")
        zip_path = self._zip_save_folder(save_folder_path, description)
        if not zip_path:
            print("[CloudSave] ERROR: Failed to create zip file.")
            return False, "Failed to create zip file."

        print(f"[CloudSave] Zip file created at: {zip_path}")
        try:
            print("[CloudSave] Attempting to upload to Google Drive...")
            self.drive_manager.upload_file(zip_path, self.cloud_folder_id)
            print("[CloudSave] Upload successful. Cleaning up local zip file.")
            os.remove(zip_path)  # Clean up the local zip file
            return True, f"Game '{description}' saved successfully to the cloud."
        except Exception as e:
            print(f"[CloudSave] ERROR: Failed to upload to Google Drive: {e}")
            return False, f"Failed to upload to Google Drive: {e}"

    def restore_save_game(self, save_folder_name):
        """Downloads a save from the cloud and then restores it locally."""
        # 1. Download the save from Google Drive
        zip_name = f"{save_folder_name}.zip"
        local_zip_path = os.path.join(self.local_manager.base_dir, zip_name)
        
        try:
            print(f"[Cloud] Downloading '{zip_name}' from Google Drive...")
            downloaded = self.drive_manager.download_file(zip_name, self.cloud_folder_id, local_zip_path)
            if not downloaded:
                return False, f"Save '{save_folder_name}' not found in the cloud."
            print(f"[Cloud] Download successful.")
        except Exception as e:
            return False, f"Cloud download failed: {e}"

        # 2. Use the local manager to restore the downloaded save
        success, message = self.local_manager.restore_save_game(save_folder_name)
        
        # Clean up the downloaded zip file
        if os.path.exists(local_zip_path):
            os.remove(local_zip_path)
            
        return success, message

    def list_save_games(self):
        """Lists save games from the cloud."""
        try:
            query = f"'{self.cloud_folder_id}' in parents and mimeType = 'application/zip' and trashed = false"
            response = self.drive_manager.service.files().list(q=query, spaces='drive', fields='files(name, createdTime, size)').execute()
            
            saves = []
            for file in response.get('files', []):
                saves.append({
                    'name': file.get('name').replace('.zip', ''),
                    'createdTime': file.get('createdTime'),
                    'size': int(file.get('size')),
                    'source': 'cloud'
                })
            
            # Sort by creation time, newest first
            saves.sort(key=lambda x: x['createdTime'], reverse=True)
            return saves
        except Exception as e:
            print(f"[Cloud] Error listing saves: {e}")
            return []

    def delete_save_game(self, save_folder_name):
        """Deletes a save game from the cloud."""
        try:
            query = f"name = '{save_folder_name}.zip' and '{self.cloud_folder_id}' in parents and trashed = false"
            response = self.drive_manager.service.files().list(q=query, spaces='drive', fields='files(id)').execute()
            files = response.get('files', [])
            
            if not files:
                return False, "Save not found in the cloud."

            file_id = files[0].get('id')
            self.drive_manager.service.files().delete(fileId=file_id).execute()
            print(f"[Cloud] Deleted '{save_folder_name}.zip' from Google Drive.")
            return True, f"Save '{save_folder_name}' deleted from the cloud."
        except Exception as e:
            return False, f"Cloud delete failed: {e}"
