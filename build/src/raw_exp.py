# Write python code to list file structure within '1_FAME_raw_data'
# If there are a large number of files in a folder following a similar structure, truncate

import os

def list_file_structure(root_dir):
    file_structure = {}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        relative_path = os.path.relpath(dirpath, root_dir)
        if relative_path == '.':
            relative_path = ''
        file_structure[relative_path] = filenames
    return file_structure