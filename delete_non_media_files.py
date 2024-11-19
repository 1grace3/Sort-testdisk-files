'''
This code sorts through a folder with lots of other subfolders and deletes all files that aren't media files.
useful when using file recovery applications like testdisk, which dumps a bunch of useless OS files
along with the media files you're trying to recover. 

Add the main folder path you want to modify below.
'''

import os

# List of media file extensions to keep
media_extensions = {'.jpg', '.jpeg', '.png', '.mov', '.mp4', '.avi', '.gif', '.bmp', '.mkv', '.mp3', '.pdf', '.docx', '.doc', '.txt'}

def delete_non_media_files(base_directory):
    """Delete all files that are not media files within the base directory and its subfolders."""
    for root, _, files in os.walk(base_directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1].lower()
            
            # If the file's extension is not in the media_extensions set, delete it
            if file_extension not in media_extensions:
                try:
                    print(f"Deleting non-media file: {file_path}")
                    os.remove(file_path)
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

if __name__ == "__main__":
    
    base_directory = r'paste the folder path here'       #modify this before running
    
    delete_non_media_files(base_directory)