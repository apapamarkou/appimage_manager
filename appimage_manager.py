#!/usr/bin/env python3

#     _                _                            
#    / \   _ __  _ __ (_)_ __ ___   __ _  __ _  ___ 
#   / _ \ | '_ \| '_ \| | '_ ` _ \ / _` |/ _` |/ _ \
#  / ___ \| |_) | |_) | | | | | | | (_| | (_| |  __/
# /_/   \_\ .__/| .__/|_|_| |_| |_|\__,_|\__, |\___|
#         |_|   |_|                      |___/      
#  __  __                                   
# |  \/  | __ _ _ __   __ _  __ _  ___ _ __ 
# | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
# | |  | | (_| | | | | (_| | (_| |  __/ |   
# |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
#
# An appimage manager solution for Linux
# Author: Andrianos Papamarkou
#

import os
import subprocess
import logging
import stat


APPLICATIONS_DIR = os.path.expanduser('~/Applications')
DESKTOP_ENTRIES_DIR = os.path.expanduser('~/.local/share/applications')
TRACKER_FILE = os.path.expanduser('~/.local/share/appimage-manager/created_desktop_entries.list')

# Ensure the tracker file exists
os.makedirs(os.path.dirname(TRACKER_FILE), exist_ok=True)
if not os.path.exists(TRACKER_FILE):
    open(TRACKER_FILE, 'w').close()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def notify(message):
    try:
        subprocess.run(['notify-send', 'AppImage Manager', message], check=True)
    except Exception as e:
        logging.error(f"Failed to send notification: {e}")

def add_to_tracker(desktop_file_path):
    with open(TRACKER_FILE, 'a') as tracker_file:
        tracker_file.write(desktop_file_path + '\n')

def remove_from_tracker(desktop_file_path):
    with open(TRACKER_FILE, 'r') as tracker_file:
        lines = tracker_file.readlines()
    with open(TRACKER_FILE, 'w') as tracker_file:
        for line in lines:
            if line.strip() != desktop_file_path:
                tracker_file.write(line)

def make_executable(file_path):
    try:
        if not os.access(file_path, os.X_OK):
            os.chmod(file_path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
            logging.info(f"Made {file_path} executable.")
    except Exception as e:
        logging.error(f"Failed to make {file_path} executable: {e}")

def create_desktop_entry(appimage_path):
    try:
        appimage_name = os.path.basename(appimage_path)
        app_name = os.path.splitext(appimage_name)[0]
        desktop_file_content = f"""[Desktop Entry]
Name={app_name}
Exec={appimage_path}
Icon=application-x-executable
Type=Application
Terminal=false
StartupWMClass={app_name}
"""
        desktop_file_path = os.path.join(DESKTOP_ENTRIES_DIR, f'{app_name}.desktop')

        # Create the .desktop file if it doesn't exist
        if not os.path.exists(desktop_file_path):
            with open(desktop_file_path, 'w') as desktop_file:
                desktop_file.write(desktop_file_content)
            logging.info(f".desktop entry created: {desktop_file_path}")
            add_to_tracker(desktop_file_path)
            notify(f"AppImage installed: {app_name}")

        # Make the .AppImage executable
        make_executable(appimage_path)

    except Exception as e:
        logging.error(f"Failed to create .desktop entry for {appimage_path}: {e}")

def remove_desktop_entry(desktop_file_path):
    try:
        if os.path.exists(desktop_file_path):
            os.remove(desktop_file_path)
            logging.info(f".desktop entry removed: {desktop_file_path}")
            remove_from_tracker(desktop_file_path)
            notify(f"AppImage removed: {os.path.splitext(os.path.basename(desktop_file_path))[0]}")
        else:
            logging.warning(f".desktop entry not found: {desktop_file_path}")
    except Exception as e:
        logging.error(f"Failed to remove .desktop entry {desktop_file_path}: {e}")

def scan_appimages():
    logging.info("Scanning for appimages...")
    try:
        appimages = {img for img in os.listdir(APPLICATIONS_DIR) if img.endswith('.AppImage')}
        appimages_base_names = {os.path.splitext(img)[0] for img in appimages}
        logging.info(f"Found appimages: {appimages_base_names}")

        desktop_entries = {entry for entry in os.listdir(DESKTOP_ENTRIES_DIR) if entry.endswith('.desktop')}
        desktop_entries_base_names = {os.path.splitext(entry)[0] for entry in desktop_entries}
        logging.info(f"Existing desktop entries: {desktop_entries_base_names}")

        new_appimages = appimages_base_names - desktop_entries_base_names
        removed_appimages = desktop_entries_base_names - appimages_base_names

        logging.info(f"New appimages: {new_appimages}")
        logging.info(f"Removed appimages: {removed_appimages}")

        # Create .desktop entries for new appimages
        for appimage in new_appimages:
            appimage_path = os.path.join(APPLICATIONS_DIR, appimage + '.AppImage')
            create_desktop_entry(appimage_path)

        # Read the tracker file to know which .desktop files were created
        with open(TRACKER_FILE, 'r') as tracker_file:
            tracked_desktop_files = set(line.strip() for line in tracker_file)

        # Remove .desktop entries for removed appimages
        for appimage in removed_appimages:
            desktop_file_path = os.path.join(DESKTOP_ENTRIES_DIR, appimage + '.desktop')
            if desktop_file_path in tracked_desktop_files:
                remove_desktop_entry(desktop_file_path)

    except Exception as e:
        logging.error(f"Failed to scan appimages: {e}")

def watch_appimages():
    logging.info("Watching for appimages...")
    try:
        process = subprocess.Popen(['inotifywait', '-m', '-e', 'create,move,delete', APPLICATIONS_DIR], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            logging.info(f"inotify event: {line.strip()}")
            scan_appimages()
    except KeyboardInterrupt:
        logging.info("Stopping watcher...")
        process.terminate()
    except Exception as e:
        logging.error(f"Error in watching appimages: {e}")

if __name__ == '__main__':
    logging.info("Starting appimage manager...")
    scan_appimages()
    watch_appimages()
