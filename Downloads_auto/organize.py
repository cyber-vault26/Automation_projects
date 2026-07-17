from pathlib import Path
import shutil

downloads = Path.home() / "Downloads"

FILE_TYPE = {
    ".pdf":"PDF",
    ".doc":"Documents",
    ".docx":"Documents",
    ".txt":"Text",
    ".jpg":"Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp3": "Music",
    ".wav": "Music",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".zip": "Archives",
    ".tar": "Archives",
    ".gz": "Archives",
    ".iso": "Disk Images",
    ".exe": "Programs",
    ".deb": "Programs",
    ".rpm": "Programs"
}

for item in downloads.iterdir():
    if item.is_file():
        category = FILE_TYPE.get(item.suffix.lower(), "others")
        
        destination = downloads / category
        destination.mkdir(exist_ok=True)
        new_path = destination / item.name

        shutil.move(item, new_path)
        print(f"Moved {item.name} --> {category}")
        