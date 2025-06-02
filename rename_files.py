# Write a script that renames all the files in a folder, 
# giving them a default name and an incrementing counter.

import os

def rename_files_in_folder(folder_path, default_name="file"):
    counter = 1
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1]
            new_name = f"{default_name}_{counter}{extension}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(file_path, new_path)
            print(f"Renamed: {filename} -> {new_name}")
            counter += 1

# Example usage:
rename_files_in_folder(r"C:\Users\escot\OneDrive\Escritorio\renamed_screenshots", "renamed_file")