import os
import shutil
from pathlib import Path

# Define the Downloads folder path
downloads_path = Path("C:/Users/User/Downloads")

# Define the subfolder structure with additional popular extensions
folders = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff', '.webp'],
    "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.csv', '.rtf', '.odt'],
    "Videos": ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm'],
    "Music": ['.mp3', '.wav', '.flac', '.aac', '.m4a', '.ogg'],
    "Archives": ['.zip', '.rar', '.7z', '.tar', '.gz', '.iso'],
    "Executables": ['.exe', '.msi', '.bat', '.cmd'],
    "Scripts": ['.py', '.js', '.html', '.css', '.php', '.sh', '.ps1'],
    "Others": []  # For all other file types
}

def organize_by_type(file):
    """Organize file by its type."""
    for folder, extensions in folders.items():
        if file.suffix.lower() in extensions:
            return folder
    return "Others"

def move_file(file, destination_folder):
    """Move file to the destination folder."""
    dest_path = downloads_path / destination_folder
    dest_path.mkdir(exist_ok=True)
    shutil.move(str(file), str(dest_path / file.name))

def organize_files():
    """Organize files in Downloads folder based on type only."""
    for file in downloads_path.iterdir():
        if file.is_file():
            # Determine the folder based on file type
            folder = organize_by_type(file)
            # Move the file to the appropriate folder
            move_file(file, folder)

# Run the organization
organize_files()
print("Files organized successfully!")
