This code is for sorting through folders with lots of subfolders and files after using data recovery tools, such as TestDisk.
Modify it however you want, I use it to delete every file that's not a media file, making it easier to sort through to find old photos/videos. 

### delete_folders.py:
This code sorts through the main folder and deletes all the subfolders that don't contain media files. (typically scripts and stuff from the OS) <br>
I recommend running this first to save time.

### delete_non_media_files.py:
This code goes through all the subfolders and separately deletes all files that are not media files. <br>
(useful when the folder contains both non-media and media.)

### To use:
Edit each file in a code editor to add the main folder path to the **base_directory** variable. <br>
ex) base_directory = r'C:\Users\yourname\RecoveredFiles'

Run each file separately.
