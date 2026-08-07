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
[] write tests for fix_excel_dates and test_check_df_matches_schema