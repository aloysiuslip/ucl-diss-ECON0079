### Environment
- Use python 3.13 or 3.12 to adapt for Windows on ARM
- `pip freeze > requirements.txt` to save installs
- `pip install -r requirements.txt` to install dependencies
Activate the virtual environment with `source venv/bin/activate` on Linux or macOS, or `venv\Scripts\activate` on Windows.
.venv should be added to .gitignore to avoid committing the virtual environment to version control.

### Database
Note that the ibis-framework package is not the same as the ibis package in PyPI. These two libraries cannot coexist in the same Python environment, as they are both imported with the ibis module name.

---
# Known bugs

[] can't get the root_dir to be in the right place
[] can't get the fame_schema to actually match what I told it