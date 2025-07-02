
import os
import shutil
import logging
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(
    description="Deletes files that don't match given extensions, and folders that contain none."
)
parser.add_argument(
    "-p", "--path", required=True,
    help="Path to the base directory to clean"
)
parser.add_argument(
    "--run", action="store_true",
    help="Actually delete files/folders (default is dry run)"
)
parser.add_argument(
    "--keep", nargs="+", required=True,
    help="List of file extensions to keep (e.g., .jpg .mp4 .pdf)"
)
args = parser.parse_args()

base_directory = args.path
dry_run = not args.run
media_extensions = set(ext if ext.startswith('.') else f'.{ext}' for ext in args.keep)

logging.basicConfig(filename='cleanup.log', level=logging.INFO, format='%(asctime)s %(message)s')


def is_kept(file_path):
    _, ext = os.path.splitext(file_path)
    return ext.lower() in media_extensions

def clean_directory_tree(base_directory, dry_run=True):
    all_dirs = [root for root, _, _ in os.walk(base_directory)]
    all_dirs.sort(key=lambda x: -len(x))  # bottom-up

    for folder in tqdm(all_dirs, desc="Cleaning folders"):
        try:
            files = [
                os.path.join(folder, f)
                for f in os.listdir(folder)
                if os.path.isfile(os.path.join(folder, f))
            ]
            keep_found = False

            for f in files:
                if is_kept(f):
                    keep_found = True
                else:
                    if dry_run:
                        print(f"[Dry Run] Would delete: {f}")
                    else:
                        os.remove(f)
                        logging.info(f"Deleted file: {f}")

            if not keep_found and not os.listdir(folder):
                if dry_run:
                    print(f"[Dry Run] Would delete folder: {folder}")
                else:
                    shutil.rmtree(folder)
                    logging.info(f"Deleted folder: {folder}")

        except Exception as e:
            logging.error(f"Error in {folder}: {e}")


if __name__ == "__main__":
    clean_directory_tree(base_directory, dry_run)