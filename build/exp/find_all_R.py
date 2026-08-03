import os
import glob
from pathlib import Path
import pandas as pd
import numpy as np
from dotenv import load_dotenv

load_dotenv(override=True)
env_data_dir = os.getenv("ROOT_DATA_DIR")
if env_data_dir is None:
	raise ValueError("ROOT_DATA_DIR environment variable is not set. Please set it in the .env file.")

pd.options.mode.chained_assignment = None  # default='warn'

# define paths
user = "lazycst"
root_dir = Path(os.getcwd()).parent.parent

work_dir = root_dir / "build/src/"
data_dir = Path(env_data_dir)						# On mobile env, set DATA_DIR in .env to "H:/Other computers/My computer/fame_clean/1_FAME_raw_data/2025.07.30"

# Iterate over every file in data_dir, including subdirectories
# And filter for files that end with .R
r_files = [f for f in data_dir.rglob('*.R')]
for r_file in r_files:
	print(f"Found R file: {r_file}")