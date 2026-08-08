# Environment
- Use python 3.13 or 3.12 to adapt for Windows on ARM
- `pip freeze > requirements.txt` to save installs
- `pip install -r requirements.txt` to install dependencies
Activate the virtual environment with `source venv/bin/activate` on Linux or macOS, or `venv\Scripts\activate` on Windows.
.venv should be added to .gitignore to avoid committing the virtual environment to version control.

### VSC keyboard shortcuts
- Jupyter: run current cell. When: `editorTextFocus && isWorkspaceTrusted && jupyter.hascodecells && !editorHasSelection && !isCompositeNotebook && !notebookEditorFocused`
- Python: run Python File in Terminal. When: `exitorTextFocus && resourceExtname =~ /\.py/i`

# Cleaning process
- Some raw sheets have primary_address missing
- Some have some columns duplicated
- The property key 'Strategy, organization and policy' has additional whitespace in some files

### Database
Note that the ibis-framework package is not the same as the ibis package in PyPI. These two libraries cannot coexist in the same Python environment, as they are both imported with the ibis module name.

---
# Known bugs

[] primary address and main distribution sites missing from some files, currently throws an error
[] write tests for handle_excel_dates and test_check_df_matches_schema
[] process yearly variables
[] cast and process geospatial data
[] review Lars data processing checklist

# TODO: loop improvements

1. Write to database batch processing.
DuckDB is columnar and built for analytical bulk operations. You should never update it row-by-row or file-by-file.

Accumulate in Memory: Instead of writing to Ibis/DuckDB in the loop, append your processed pandas DataFrames to a list (batch_dfs.append(df_fixed_one_dates)).

Batch Writes: Every set of industry files files (or at the very end of the script), concatenate the list using pd.concat(batch_dfs) and write that chunk to the database using an append operation or a single massive upsert.
Every time your loop hits con.create_table("fame_fixed", table_updated_fixed_raw, overwrite=True), DuckDB has to freeze, read the existing database state, execute an anti-join across the entire table, append the new rows, and overwrite the file on your disk. As the table grows, that 1.12 seconds will balloon to 5 seconds, then 10 seconds per file.

The Fix: In-Memory Batching
We need to rip Ibis and DuckDB out of your inner loop entirely.
The loop should only be responsible for using pandas to read the Excel file, clean the columns, and append the resulting DataFrame to a list. Once the loop is finished, we staple all 12,846 DataFrames together using pd.concat(), and write to DuckDB exactly once.

Here is how you need to restructure the bottom half of that cell in main_clean.ipynb:

2. Multiprocessing (The Ultimate Speedup)
Because processing one FAME file has absolutely no dependency on the next one, this task is "embarrassingly parallel."

The Fix: Parallel Execution
Instead of a standard for loop, you can use Python's concurrent.futures.ProcessPoolExecutor. You can have 4, 8, or 16 worker processes (depending on your CPU) reading Excel files and parsing them into pandas DataFrames simultaneously. You would then collect these DataFrames and do a single, bulk write to DuckDB on your main thread.

Fixing the database loop (Point 1) and switching to Calamine (Point 2) alone should easily cut your processing time down from hours to minutes.

If 15 minutes is still too slow, you can layer multiprocessing on top of the batching. The trick is to artificially throttle it to protect your RAM. Instead of using all 16 threads, you would tell Python's ProcessPoolExecutor to use exactly 4 workers. Those 4 workers read the files, and the main thread collects them into the industry batch for writing.