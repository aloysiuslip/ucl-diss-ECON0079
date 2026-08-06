import os
from pathlib import Path
from dotenv import load_dotenv
from typing import NamedTuple

class DirPaths(NamedTuple):
	root_data_dir: Path | None
	data_dir: Path | None
	raw_data_dir: Path | None
	root_dir: Path
	work_dir: Path
	output_dir: Path
     
def get_data_dirs() -> DirPaths:

    # Load dir paths from .env file
    load_dotenv(override=True)

    env_data_dir = os.getenv("DATA_DIR")
    env_root_data_dir = os.getenv("ROOT_DATA_DIR")

    try:
        if env_data_dir is None:
            raise ValueError("DATA_DIR environment variable is not set.")
        data_dir = Path(env_data_dir)
        if not data_dir.exists() or not data_dir.is_dir():
            raise ValueError(f"DATA_DIR path does not exist or is not a directory: {data_dir}")

        if env_root_data_dir is None:
            raise ValueError("ROOT_DATA_DIR environment variable is not set.")
        root_data_dir = Path(env_root_data_dir)
        if not root_data_dir.exists() or not root_data_dir.is_dir():
            raise ValueError(f"ROOT_DATA_DIR path does not exist or is not a directory: {root_data_dir}")

    # Don't hang on a ValueError, just print it and then return an empty string from the overall function
    except ValueError as e:
        print(f"❌ {e}")

    data_dir = Path(env_data_dir) if env_data_dir else None
    root_data_dir = Path(env_root_data_dir) if env_root_data_dir else None
    raw_data_dir = root_data_dir / "1_FAME_raw_data" / "2025.02" if root_data_dir else None

    # Load some dir paths from the current script's parent directory
    user = "lazycst"
    file_path = Path(__file__).resolve()            # the absolute path to the current script
    root_dir = file_path.parent.parent.parent
    work_dir = root_dir / "build" / "src"
    output_dir = root_dir / "build" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    return DirPaths(root_data_dir, data_dir, raw_data_dir, root_dir, work_dir, output_dir)

# If this file is run as a script, then call the function and print the results
if __name__ == "__main__":
    dirs = get_data_dirs()

    # Print every item in the dirs dictionary
    # But 'DirPaths' object has no attribute 'items'
    # Iterate over them
    for attr in dir(dirs):
        if attr.startswith('_'):
            continue
        if callable(getattr(dirs, attr)):
            continue

        print(f"{attr}: {getattr(dirs, attr)}")
