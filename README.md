# Environment
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
- Cleaned some columns which stored 'nan' as string

### Data
- 2 million rows in fame_fixed and fame_derived
- 14 million rows in fame_yearly, which means a mean of 7 years available per firm entry

### Database
Note that the ibis-framework package is not the same as the ibis package in PyPI. These two libraries cannot coexist in the same Python environment, as they are both imported with the ibis module name.
- We engineer the loop to load first, and then write on each batch transforming with panda.
- This is done so transformations are done in RAM with one I/O per industry.
- This means less I/O writes to stop the hard drive being the bottleneck

---
### FIX known bugs
1h2m runtime in priority list
- Memory error years: 47, 74. 43, some error

### TODO
[] migrate ingest to get rid of fame_derived completely
[] cast and process geospatial data
