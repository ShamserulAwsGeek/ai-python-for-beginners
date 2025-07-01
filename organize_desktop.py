import os
import shutil
from pathlib import Path

# Define categories and associated file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".tiff"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".ppt", ".xlsx", ".xls", ".odt"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".ps1"]
}

# Get desktop path for current user
DESKTOP_PATH = Path.home() / "Desktop"

def organize_files(base_path=DESKTOP_PATH):
    if not base_path.exists():
        print(f"Path does not exist: {base_path}")
        return

    for item in os.listdir(base_path):
        item_path = base_path / item

        if item_path.is_file():
            file_ext = item_path.suffix.lower()
            moved = False

            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    target_folder = base_path / category
                    target_folder.mkdir(exist_ok=True)
                    shutil.move(str(item_path), str(target_folder / item))
                    print(f"Moved: {item} → {category}/")
                    moved = True
                    break

            if not moved:
                other_folder = base_path / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(item_path), str(other_folder / item))
                print(f"Moved: {item} → Others/")

if __name__ == "__main__":
    organize_files()
