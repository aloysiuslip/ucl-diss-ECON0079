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
    # Build root dir based on the location of the current script, which is in build/src
    root_dir = Path(__file__).parent.parent
    print(f"Current script's parent directory: {Path(__file__)}")
    
    print(root_dir)
    print(f"Root directory: {root_dir}")
    work_dir = root_dir / "build" / "src"
    output_dir = root_dir / "build" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # return data_dir, root_data_dir, root_dir, work_dir, output_dir

    # Above is a tuplet return of all the possible dir paths
    # If I wanted to return a named output variable from this function
    # ex: calling it would be {root_dir} = get_data_dirs()
    # obviously not necessarily in that exact syntax
    # Then the viability of doing that in python is questionable,
    # but I could return a dictionary instead of a tuplet
    # The most concise way to do that below
    # without having to duplicate writing out keys and values is:
    # return {k: v for k, v in locals().items() if isinstance(v, Path) or v is None}

    # Alternatively, return an output which I can access as output.data_dir
    # when calling this function
    return DirPaths(root_data_dir, data_dir, raw_data_dir, root_dir, work_dir, output_dir)