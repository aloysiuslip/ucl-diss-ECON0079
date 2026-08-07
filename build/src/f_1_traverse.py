from pathlib import Path

# Define a function with types which takes a directory path (string)
# And returns a dictionary of [industry, object] key-value pairs
# Where industry is a 2-digit SIC (e.g., "01", "02", etc.)
# And object is a dictionary containing the following keys:
# a1_ID, a2_key_finance, a3_assets, a4_profits, and a5_misc.
# where the values of this dictionary are the corresponding file paths
# under each of the subdirectories of of the industry/key,
# ex: /01/a1_ID, /01/a2_key_finance

# Declare a 'RawFileDict' type for the return value of the function
RawFileDict = dict[str, dict[str, list[str]]]

def build_raw_file_dict(dir: Path) -> RawFileDict:

    raw_file_dict = {}
    errors = []
    passed_inds = ['Traversing industry directory: ']

    for industry_dir in dir.iterdir():

        if not industry_dir.is_dir():
            errors.append(f"Expected directory but found file: {industry_dir.name}")
            continue

        # Check if the directory name is a 2-digit SIC code
        if not industry_dir.name.isdigit() or len(industry_dir.name) != 2:
            errors.append(f"Expected 2-digit SIC code but found: {industry_dir.name}")
            continue

        if len(passed_inds) == 1 and passed_inds[0] == 'Traversing industry directory: ':
            passed_inds[0] = f"Traversing industry directory: {industry_dir.name}"
        else:
            passed_inds.append(industry_dir.name)
        print(f"\r{', '.join(passed_inds)}", end="", flush=True)
        if len(passed_inds) % 15 == 0 and len(passed_inds) > 0:
            print('')
            passed_inds = []

        industry = industry_dir.name
        raw_file_dict[industry] = {}
        for key_dir in industry_dir.iterdir():
            # ex: [data_dir]/01/a1_ID, [data_dir]/01/a2_key_finance, etc.

            if not key_dir.is_dir():
                errors.append(f"Expected directory but found file: {key_dir.name}")
                continue

            key = key_dir.name

            if key not in raw_file_dict[industry]:
                raw_file_dict[industry][key] = []
            for file in key_dir.iterdir():
                if not file.is_file():
                    errors.append(f"Expected file but found directory: {file.name}")
                    continue

                if not file.name.endswith(".xlsx"):
                    errors.append(f"Expected .xlsx file but found: {file.name}")
                    continue

                if not file.name.startswith("Export"):
                    errors.append(f"Rogue file found: {file.name} in {key_dir.name}")
                    continue

                # Store the file path in the dictionary
                raw_file_dict[industry][key].append([
                    str(file.name),
                    str(file)
                ])

    if len(errors) > 0:
        for error in errors:
            # Error file is this script's parent directory /output/traverse_errors.txt
            error_file = Path(__file__).parent.parent / "output" / "traverse_errors.txt"
            with open(error_file, "w") as f:
                f.write("Errors found:\n")
                f.write(error + "\n")

    print('')
    return raw_file_dict

import pandas as pd
from f_0_dirs import get_data_dirs
dirs = get_data_dirs()

if __name__ == "__main__":

    pd.options.mode.chained_assignment = None

    if dirs.raw_data_dir is None:
        raise ValueError("❌ RAW_DATA_DIR environment variable is not set or is invalid. Please check your .env file.")

    raw_file_dict = build_raw_file_dict(dirs.raw_data_dir)
    # with open(dirs.output_dir / "raw_file_dict.json", "w") as f:
    #     json.dump(raw_file_dict, f, indent=4)
    print(f"✅ Successfully built raw file dictionary and saved to: {dirs.output_dir / 'raw_file_dict.json'}")