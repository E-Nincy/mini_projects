#Write a script that walks through a nested folder structure and prints 
# out all the Python files that it can find.

import os

def find_python_files(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith("py"):
                full_path = os.path.join(dirpath, file)
                print(full_path)

# Print python files:
find_python_files(r"C:\Users\escot\OneDrive\Escritorio\Codingnomads")
