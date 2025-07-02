
# 🧼 Smart Folder Cleaner (Extension Based)

This script **deletes files and folders** that don’t match the extensions you specify. Good for sorting folders after using recovery tools like Testdisk, sorting backups, or dumps.

---

## 📦 Requirements

- Python 3.6+
- tqdm (`pip install tqdm`)

---

## How to Use

### 1. Install Requirements

Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)  
Make sure to check **"Add Python to PATH"** during installation.

Install tqdm by Open Command Prompt and run:
```bash
pip install tqdm
```

### 2. Run the script

It's recommended to first do a dry run: (default)
```bash
python clean.py -p "C:\Path\To\Folder" --keep .jpg .png .mp4
```
To actually delete files and folders add run argument:
```bash
python clean.py -p "C:\Path\To\Folder" --run --keep .jpg .png .mp4
```

### ✅ You're Done

- Once finished it will generate a cleanup.log file in the same directory as the script
- Running multiple times will append to the log file.


## 📎Notes
- You can use any extension with --keep, not just media.
For example, to keep only .doc files:
```bash
python clean.py -p "D:\Docs" --run --keep .doc
```
- Extensions must include the dot (e.g., .jpg, not jpg).

- Files with no extension are treated as deletable.

- If you see an error like:
```bash
ModuleNotFoundError: No module named 'tqdm'
```
Just run `pip install tqdm` and re-run the command

- Specifying your path with **-p** is **required**

- Specifying the extension names you would like to keep with **--keep** is **required**