# File Type Counter

from pathlib import Path
from pprint import pprint, pformat
import shutil

# Locate  Desktop
desktop_path = Path.home() / "OneDrive" / "Escritorio"

# Get all files on the Desktop (not folders)
files = [file for file in desktop_path.iterdir() if file.is_file()]

# Count files
file_type_counts = {}

for file in files:
    suffix = file.suffix.lower()  # e.g. '.png', '.txt'
    if suffix in file_type_counts:
        file_type_counts[suffix] += 1
    else:
        file_type_counts[suffix] = 1

#  Print the results
print("File type counts on your Desktop:")
pprint(file_type_counts)

# New code that writes to a file
output_path = Path("filecounts.txt")
with open(output_path, "w", encoding="utf-8") as file_out:
    file_out.write("File type counts on your Desktop:\n")
    file_out.write(pformat(file_type_counts))