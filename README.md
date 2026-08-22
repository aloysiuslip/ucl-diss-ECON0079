# Environment
- `pip freeze > requirements.txt` to save installs
- `pip install -r requirements.txt` to install dependencies
Activate the virtual environment with `source venv/bin/activate` on Linux or macOS, or `venv\Scripts\activate` on Windows.
.venv should be added to .gitignore to avoid committing the virtual environment to version control.
- Pass `fame_data.duckb` and `descriptives/input/skinny_NSPL_MAY_2026_UK.xlsx` back and forth

### VSC keyboard shortcuts
- Jupyter: run current cell. When: `editorTextFocus && isWorkspaceTrusted && jupyter.hascodecells && !editorHasSelection && !isCompositeNotebook && !notebookEditorFocused`
- Python: run Python File in Terminal. When: `exitorTextFocus && resourceExtname =~ /\.py/i`

# Build - data cleaning
- Some raw sheets have primary_address missing
- Some have some columns duplicated
- The property key 'Strategy, organization and policy' has additional whitespace in some files
- Cleaned some columns which stored 'nan' as string

### Data
- 2 million rows in fame_fixed and fame_derived
- raw: 48 million rows in fame_yearly. Down to 47.4 million after using a max merge strategy, removing 1.3m
- 

### Database
Note that the ibis-framework package is not the same as the ibis package in PyPI. These two libraries cannot coexist in the same Python environment, as they are both imported with the ibis module name.
- We engineer the loop to load first, and then write on each batch transforming with panda.
- This is done so transformations are done in RAM with one I/O per industry.
- This means less I/O writes to stop the hard drive being the bottleneck

# Descriptives
### TODO
- [ ] Verify spatial: calculate lat lon from postcode, and then from raw lat long
- [ ] Compare them to check cases
- [ ] Understand distance generation process. Currently, we have some errors
- Both in generating distances within a postcode ()
  
# Model
### TODO
- [X] Basic TFP panel regression
- [X] LLM model 1: group TFP averages calculated  
- [X] LLM model 1: run panel regression with these group averages  
- [X] LLM model 1: run panel with industry vs non-industry groups too (6 more donut groups)
- [X] Distance model 2: calculated distances  
- [ ] Distance model 2: run panel regression with distances  
- [X] Dynamic model 3: installed and tested the python package  
- [ ] Dynamic model 3: run and play with LLM in dynamic set-up  
