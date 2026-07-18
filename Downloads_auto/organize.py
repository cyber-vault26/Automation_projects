from pathlib import Path
import shutil
import logging

logging.basicConfig(
    filename="orgarnizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

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

stats = {}
total_file = 0

for item in downloads.iterdir():
    if not item.is_file():
        continue
    if item.name.startswith("."):
        continue
    total_file += 1

    category = FILE_TYPE.get(item.suffix.lower(), "others")
        
    destination = downloads / category
    destination.mkdir(exist_ok=True)
    new_path = destination / item.name

    counter = 1

    while new_path.exists():
        new_path = (
            destination / f"{item.stem}_{counter}{item.suffix}"
        )

    shutil.move(str(item), str(new_path))

    logging.info(
        f"Moved {item.name} -> {new_path}"
    )
    stats[category] = stats.get(category, 0) + 1

#summary of the report
print("="*50)
print("DOWNLOADS ORGANIZER REPORT")
print("="*50)

print(f"Total files processed: {total_file}")

print()

for category in sorted(stats):
    print(f"{category:>20} {stats[category]}")
print()

print("Organization complete!")

logging.info("Organization finished succesfull")
        