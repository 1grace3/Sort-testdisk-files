'''
This code sorts through a folder with lots of other subfolders and deletes all the subfolders without media files.
useful when using file recovery applications like testdisk, which partitions files into folders, 
some of which don't have any media files you're trying to recover. 

Add the main folder path you want to modify below.
'''

import os
import shutil


media_extensions = {'.jpg', '.jpeg', '.png', '.mov', '.mp4', '.mp3', '.gif', '.bmp', '.avi', '.mkv'}

def contains_media_files(folder):
    """Check if the folder contains any media files."""
    for root, _, files in os.walk(folder):
        for file in files:
            if os.path.splitext(file)[1].lower() in media_extensions:
                return True
    return False

def delete_empty_folders(base_directory):
    for root, dirs, _ in os.walk(base_directory, topdown=False):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if not contains_media_files(folder_path):
                try:
                    print(f"Deleting empty folder: {folder_path}")
                    shutil.rmtree(folder_path)
                except Exception as e:
                    print(f"Error deleting {folder_path}: {e}")

if __name__ == "__main__":
    # Set the base directory you want to search
    base_directory = r'paste the folder path here'
    
    delete_empty_folders(base_directory)