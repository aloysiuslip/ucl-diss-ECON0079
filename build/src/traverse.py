import os
from pathlib import Path

# Define a function with types which takes a directory path (string)
# And returns a dictionary of [industry, object] key-value pairs
# Where industry is a 2-digit SIC (e.g., "01", "02", etc.)
# And object is a dictionary containing the following keys:
# a1_ID, a2_key_finance, a3_assets, a4_profits, and a5_misc.
# where the values of this dictionary are the corresponding file paths
# under each of the subdirectories of of the industry/key,
# ex: /01/a1_ID, /01/a2_key_finance

def build_raw_file_dict(data_dir: str) -> dict[str, dict[str, str]]:

    raw_file_dict = {}
    errors = []

    for industry_dir in Path(data_dir).iterdir():
        # ex: /01, /02, etc.

        if not industry_dir.is_dir():
            errors.append(f"Expected directory but found file: {industry_dir}")
            continue

        # Check if the directory name is a 2-digit SIC code
        if not industry_dir.name.isdigit() or len(industry_dir.name) != 2:
            errors.append(f"Expected 2-digit SIC code but found: {industry_dir.name}")
            continue

        industry = industry_dir.name
        raw_file_dict[industry] = {}
        for key_dir in industry_dir.iterdir():
            # ex: a1_ID, a2_key_finance, a3_assets, a4_profits, a5_misc

            if not key_dir.is_dir():
                errors.append(f"Expected directory but found file: {key_dir}")
                continue

            key = key_dir.name

            for file in key_dir.iterdir():
                if not file.is_file():
                    errors.append(f"Expected file but found directory: {file}")
                    continue

                # Store the file path in the dictionary
                raw_file_dict[industry][key] = str(file)

    if errors:
        print("Errors found:")
        for error in errors:
            print(f" - {error}")

    return raw_file_dict
