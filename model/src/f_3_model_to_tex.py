import re
import pandas as pd
from pathlib import Path

from typing import TypedDict

from pytest import param
from f_3a_parse_linear import get_stars

class ParamEstimate(TypedDict):
    coef: str
    se: str
    stars: str

class ModelResult(TypedDict):
    Y: str
    params: dict[str, ParamEstimate]
    struct_params: list[str]
    obs: str
    time_nb: str
    entities_nb: str
    time_fe: bool
    entities_fe: bool
    r2: str
    use_struct: bool
    # "r2-overall": str

# Calculate the adjusted R-squared value.

# Parameters:
# - r2: The original R-squared value.
# - nobs: The number of observations.
# - nparams: The number of parameters in the model.

# Returns:
# - The adjusted R-squared value.
def calc_r2_adj(r2: float, nobs: int, nparams: int) -> float:
    if nobs <= nparams + 1:
        raise ValueError("Number of observations must be greater than number of parameters + 1 for adjusted R-squared calculation.")
    
    r2_adj = 1 - (1 - r2) * (nobs - 1) / (nobs - nparams - 1)
    return r2_adj

# Parses lowercase string variable names into LaTeX formatted matrix transformations
# Handles compound matrices, exponents, subscripts, and trailing vectors
def format_transf(var_name: str) -> str:
    # Fallback if the variable doesn't match the expected underscore pattern
    if '_' not in var_name:
        return var_name 
        
    # 1. Split the string at the last underscore
    matrix_part, vector_part = var_name.rsplit('_', 1)
    
    # 2. Format the vector part (lowercase, bold)
    vec_latex = f"\\mathbf{{{vector_part}}}"
    
    # 3. Define the regex replacement logic for the matrix part
    def matrix_replacer(match):
        base = match.group(1).upper()
        exponent = match.group(2)
        subscript = match.group(3)
        
        latex = f"\\mathbf{{{base}}}"
        if exponent:
            latex += f"^{{{exponent}}}"
        if subscript:
            latex += f"_{{{subscript}}}"
        return latex
        
    # Regex explanation:
    # Group 1: ([wvi]) captures specific base matrix letters (w, v, i)
    # Group 2: (\d+)? optionally captures an exponent number (e.g., '2', '3')
    # Group 3: ([gd]\d+)? optionally captures a subscript pattern (e.g., 'g1', 'd3')
    matrix_pattern = re.compile(r"([wvi])(\d+)?([gd]\d+)?", re.IGNORECASE)
    
    # Apply the regex to the matrix part
    mat_latex = matrix_pattern.sub(matrix_replacer, matrix_part)
    
    # Clean up formatting for subtraction operations (adds proper mathematical spacing)
    mat_latex = mat_latex.replace('-', ' - ')
    
    # 4. Combine into final LaTeX string
    return f"${mat_latex}{vec_latex}$"

# ==========================================
# Example Usage Tests
# ==========================================
# print(format_transf("wg3_y"))          -> $\mathbf{W}_{g3}\mathbf{y}$
# print(format_transf("w2g1_k"))         -> $\mathbf{W}^2_{g1}\mathbf{k}$
# print(format_transf("wg1wg2_k"))       -> $\mathbf{W}_{g1}\mathbf{W}_{g2}\mathbf{k}$
# print(format_transf("(i-wg1)w2g1_k"))  -> $(\mathbf{I} - \mathbf{W}_{g1})\mathbf{W}^2_{g1}\mathbf{k}$

if __name__ == "__main__":
    test_vars = [
        "wg3_y", "w2g1_k", "wg1wg2_k", "(i-wg1)w2g1_k",
        "v3d2_l", "i_wg1wg2_y", "w3g1wg2_k"
    ]
    should_vars = [
        "$\\mathbf{W}_{g3}\\mathbf{y}$",
        "$\\mathbf{W}^2_{g1}\\mathbf{k}$",
        "$\\mathbf{W}_{g1}\\mathbf{W}_{g2}\\mathbf{k}$",
        "$(\\mathbf{I} - \\mathbf{W}_{g1})\\mathbf{W}^2_{g1}\\mathbf{k}$",
        "$\\mathbf{V}^3_{d2}\\mathbf{l}$",
        "$\\mathbf{I}\\mathbf{W}_{g1}\\mathbf{W}_{g2}\\mathbf{y}$",
        "$\\mathbf{W}^3_{g1}\\mathbf{W}_{g2}\\mathbf{k}$"
    ]
    out_vars = [format_transf(v) for v in test_vars]
    for v, o, s in zip(test_vars, out_vars, should_vars):
        try:
            assert o == s, f"Expected {s}, got {o}"
            print(f"PASSED: {v} -> {o}")
        except AssertionError as e:
            print(f"FAILED: {v} -> {o}, expected {s}")
            print(e)

# Formats a parameter string for LaTeX based on a renaming strategy
# Merges explicit dictionary/string instructions with automated regex parsing
# Safely escapes underscores in plaintext to prevent LaTeX compilation errors
def format_latex_column(col: str, rename_strat: dict | str | None = None, mod: ModelResult | None = None) -> str:
    val = str(col)
    
    # 1. Dictionary mapping strategy
    if isinstance(rename_strat, dict) and col in rename_strat:
        return rename_strat[col]
        
    # 2. String instruction strategy
    if isinstance(rename_strat, str):
        if rename_strat == 'none' or (val.startswith("$") and val.endswith("$")):
            # Leave pre-formatted math mode alone, safely escape others
            return val if val.startswith("$") else val.replace('_', '\\_')

        elif rename_strat == 'itx':
            return f"$\\itx{{{val.replace('_', '\\_')}}}$"

        elif rename_strat == 'struct':
            if (
                mod is not None and 'struct_params' in mod and
                len(mod['struct_params']) > 0 and
                col not in mod['struct_params']
            ):
                return format_latex_column(col, rename_strat='none')
            else:
                return f"$\\{val}$"
            
        elif rename_strat == 'matrix':
            if (
                mod is not None and 'struct_params' in mod and
                len(mod['struct_params']) > 0 and
                col not in mod['struct_params']
            ):
                return format_latex_column(col, rename_strat='none')
            else:
                return format_transf(val) 
            
        elif rename_strat == 'equation':
            sections = val.split('_')
            if "{" in val and "}" in val:
                return f"${val}$"
            elif len(sections) > 1:
                return f"${sections[0]}_{{{sections[1]}}}$"
            else:
                return f"${val}$"
                
    # 3. Automated regex parsing (Fallback)
    if val == 'const':
        return 'constant'

    d: dict[str, str] = {'core': val}
    
    if 'ln_' in val:
        d['ln_start'] = 'ln(\\itx{'
        d['ln_end'] = '})'
        d['core'] = d['core'].replace('ln_', '')

    lag_match = re.match(r'L(\d+)\.(.+)', d['core'])
    if lag_match:
        lag_num = lag_match.group(1)
        d['lag'] = f"t-{lag_num}"
        d['core'] = lag_match.group(2)

    num_match = re.match(r'(.+?)(\d+)$', d['core'])
    if num_match:
        d['core'] = num_match.group(1)
        d['num'] = num_match.group(2)

    i_match = re.match(r'(.+?)_([ijk])$', d['core'])
    if i_match:
        d['core'] = i_match.group(1)
        d['index'] = i_match.group(2)
    
    insub_props = ['num']
    insub_v = [d.get(prop) for prop in insub_props if d.get(prop) is not None]
    insubscript_str = f"\\textsubscript{{${','.join(insub_v)}$}}" if insub_v else ''

    outsub_props = ['index', 'lag']
    outsub_v = [d.get(prop) for prop in outsub_props if d.get(prop) is not None]
    outsubscript_str = f"\\textsubscript{{${','.join(outsub_v)}$}}" if outsub_v else ''
    
    final_str = "".join([
        d.get('ln_start', ''),
        f"\\itx{{{d.get('core', '')}}}",
        insubscript_str,
        d.get('ln_end', ''),
        outsubscript_str
    ])
    
    # Apply a final sweep to escape any remaining underscores outside of math mode
    return final_str.replace('_', '\\_')

# Generates the \lblock or \cblock LaTeX macros for the table
def form_block(
        args: tuple | None = None,
        block_type: str = 'l',
        size: tuple | str | None = None
    ) -> str:
    # Make the block an arbitrary size. Add a row for every entry in the tuple
    arg_list = list(args) if args else []
    size_list = [None] * len(arg_list)
    if isinstance(size, str):
        size_list = [size] * len(arg_list)
    elif isinstance(size, tuple):
        size_list = list(size) + [None] * (len(arg_list) - len(size))
    content_arr =  []

    for line, s in zip(arg_list, size_list):
        if line:
            content_arr.append(f"\t\t\t\\{s}{{{line}}} \n" if s else f"\t\t\t{line} \n")
    content_str = "\t\t\t\\\\\n".join(content_arr) if content_arr else ""

    return "".join([
        f"\\makecell[t{block_type}]{{\n"
        f"{content_str}",
        f"\t\t}}"
    ])

# Constructs the test result block for pydynpd models.
def build_fe(is_present: bool | None) -> str:
    if is_present is None:
        return " "
    symbol = "\\checkmark" if is_present else "~"
    return symbol

# Constructs the test result block for pydynpd models.
def build_test_cblock(reject: bool | None, p_val: str) -> str:
    if reject is None or not p_val:
        return " "
    symbol = "\\checkmark" if reject else "\\text{\\sffamily X}"
    star_str = get_stars(p_val)
    return form_block(
        (symbol, f"({p_val}){star_str}"),
        block_type='c',
        size=(None, 'footnotesize')
    )


# Combines models into a final .tex table.
def generate_latex_table(
        models: dict[str, ModelResult],
        output_filepath: str | Path,
        show: list[int] | None = None,
        rename_strat: str | dict[str, str] | None = None,
        hide_fe: bool | None = False,
        var_order: list[str] | None = None,
        use_colnames: bool = True,
        start_at: int | None = 1,
        stars: bool = True,
        r2_type: list[str] = ['r2', 'r2-overall'],
    ) -> None:

    if hide_fe is None:
        hide_fe = False
    if start_at == None or start_at < 1:
        start_at = 1
    if stars is None:
        stars = True
    if r2_type is None:
        r2_type = ['r2', 'r2-overall']
    start_index = start_at - 1

    # If the show parameter is provided, filter the models to only include those indices
    if show is not None:
        model_names = list(models.keys())
        filtered_m_names = [model_names[i - 1] for i in show]
        filtered_models = {name: models[name] for name in filtered_m_names}
        models = filtered_models

    # Add an indicator property to each model to denote whether it is a structural model or not, based on the presence of 'struct_params'
    for mod in models.values():
        mod['use_struct'] = 'struct_params' in mod and bool(mod['struct_params'])

    model_names = list(models.keys())
    unique_params = []
    for mod in models.values():
        param_list = mod['struct_params'] if mod['use_struct'] else list(mod['params'].keys())
        to_add = [p for p in param_list if p not in unique_params]
        unique_params.extend(to_add)
    sorted_params = unique_params
    if isinstance(rename_strat, dict):
        renamed_params = list(rename_strat.keys())
        sorted_params = renamed_params + [p for p in sorted_params if p not in renamed_params]
    if var_order:
        sorted_params = var_order + [p for p in sorted_params if p not in var_order]
    sorted_params = [p for p in sorted_params if p in unique_params]
    sorted_params.remove('const') if 'const' in unique_params else None
    sorted_params.insert(0, 'const') if 'const' in unique_params else None
    seen = set()
    sorted_params = [x for x in sorted_params if not (x in seen or seen.add(x))]

    latex_lines = [f"\\begin{{tabular}}{{l{'c' * len(model_names)}}}"]
    
    # Header row
    cols = [form_block()]
    for i, mod in enumerate(model_names):
        y_str = format_latex_column(models[mod].get('Y', 'Y'), None, models[mod])
        display_name = mod if use_colnames else y_str
        cols.append(form_block((f"({start_index + i + 1}.)", display_name), block_type='c', size=('small', 'footnotesize')))
    latex_lines.extend(["\t\t\\toprule\\toprule", " & ".join(cols) + " \\\\[0.8em]", "\t\t\\toprule"])

    # Coefficients
    for param in sorted_params:
        param_display = format_latex_column(param, rename_strat, models[model_names[0]])
        row_lines = [form_block((param_display, '~'))]
        for mod in model_names:
            param_list = models[mod]['struct_params'] if models[mod]['use_struct'] else list(models[mod]['params'].keys())
            if param not in param_list:
                row_lines.append(" ")
                continue
            mod_data = models[mod]['params'].get(param)
            if mod_data:
                cblock = form_block(
                    (
                        f"${mod_data['coef']}$",
                        f"({mod_data['se']}){mod_data['stars'] if stars else ''}"
                    ),
                    block_type='c',
                    size=(None, 'footnotesize')
                )
                row_lines.append(cblock)
            else:
                row_lines.append(" ")
        latex_lines.extend([" & ".join(row_lines), "\t\t\\\\ [0.9em]"])

    # Summary and Test Statistics
    latex_lines.append("\t\t\\hline")
    
    # Handle GMM Test rows if they exist in the model dictionary
    has_gmm_tests = any('hansen_p' in m and m['hansen_p'] for m in models.values())
    if has_gmm_tests:
        for test_key, test_name in [('hansen', 'J-test'), ('ar1', 'AR(1) test'), ('ar2', 'AR(2) test')]:
            # Only display the test row if at least one model has the test results
            if all(models[m].get(f'{test_key}_reject') is None for m in model_names):
                continue
            cells = [build_test_cblock(models[m].get(f'{test_key}_reject'), models[m].get(f'{test_key}_p', '')) for m in model_names]
            latex_lines.append(f"\t\t{form_block((test_name, None))} & " + " & ".join(cells) + "\n\t\t\\\\ [0.9em]")
        latex_lines.append("\t\t\\hline")

    # Observations, time, entities
    i_row = "\t\t\\textit{i} F.E. & " + " & ".join([build_fe(models[m].get('entities_fe')) for m in model_names]) + "\n\t\t\\\\"
    t_row = "\t\t\\textit{t} F.E. & " + " & ".join([build_fe(models[m].get('time_fe')) for m in model_names]) + "\n\t\t\\\\"
    obs_row = "\t\tObs. & " + " & ".join([models[m].get('obs') for m in model_names]) + "\n\t\t\\\\"
    # Only add the i_row if there is at least one model with a non-empty entities_fe
    
    if any(models[m].get('instruments') for m in model_names):
        # instr_row = "\t\tInstruments & " + " & ".join([models[m].get('instruments', []) for m in model_names]) + "\n\t\t\\\\"
        # Construct instr_row model by model
        instr_row = "\t\t\\footnotesize{Instr.} & "
        for m in model_names:
            instr_list = models[m].get('instruments', [])
            if instr_list:
                instr_transf = [format_transf(x) for x in instr_list]
                instr_mod_tup = tuple([", ".join(instr_transf[i:i + 2]) for i in range(0, len(instr_transf), 2)])
                instr_mod_block = form_block(instr_mod_tup, block_type='c', size='footnotesize')
                instr_str = instr_mod_block
            else:
                instr_str = "~"
            instr_row += instr_str + " & "
        instr_row = instr_row.rstrip(" & ") + "\n\t\t\\\\"
        latex_lines.append(instr_row)
    if hide_fe != False and any(models[m].get('entities_fe') for m in model_names):
        latex_lines.append(i_row)
    if hide_fe != False and any(models[m].get('time_fe') for m in model_names):
        latex_lines.append(t_row)
    if any(models[m].get('obs') for m in model_names):
        latex_lines.append(obs_row)
    

    # Handle R-squared if it exists (for standard OLS models)
    r2_type_list = [t.replace('-adj', '') for t in r2_type]
    has_r2 = 'r2' in r2_type_list and any('r2' in m and m['r2'] for m in models.values())
    has_r2_overall = 'r2-overall' in r2_type_list and any('r2-overall' in m and m['r2-overall'] for m in models.values())
    if has_r2:
        r2_vals = []
        should_adj = 'r2-adj' in r2_type
        for m in model_names:
            mod = models[m]
            raw_val = float(mod.get('r2', ''))
            try:
                float_val = float(raw_val)
            except ValueError:
                float_val = 0.0
            nobs = int(mod.get('obs', 0).replace(',', ''))
            nparams = len(mod.get('params', {}))
            if should_adj:
                r2_vals.append(calc_r2_adj(float_val, nobs, nparams))
            else:
                r2_vals.append(float_val)
        r2_formatted = [f"{v:.4f}" for v in r2_vals]
        r2_row = "".join([
            f"\t\tR$^2${"-adj" if should_adj else ''}{" (excl. F.E.)" if has_r2_overall else ''} & ",
            " & ".join(r2_formatted),
            "\n\t\t\\\\"
        ])
        latex_lines.append(r2_row)
        
    if has_r2_overall:
        r2o_vals = []
        should_adj = 'r2-overall-adj' in r2_type
        for m in model_names:
            mod = models[m]
            try:
                raw_val = float(mod.get('r2-overall', ''))
            except ValueError:
                raw_val = 0.0
            nobs = int(mod.get('obs', 0).replace(',', ''))
            nparams = len(mod.get('params', {}))
            if should_adj:
                r2o_vals.append(calc_r2_adj(raw_val, nobs, nparams))
            else:
                r2o_vals.append(raw_val)
        r2o_formatted = [f"{v:.4f}" for v in r2o_vals]
        r2o_row = "".join([
            f"\t\tR$^2${"-adj" if should_adj else ''} (Overall) & ",
            " & ".join(r2o_formatted),
            "\n\t\t\\\\"
        ])
        latex_lines.append(r2o_row)

    latex_lines.extend(["\t\t\\bottomrule", "\t\\end{tabular}"])

    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(latex_lines))
    print(f"Successfully generated LaTeX table with {len(model_names)} models at {output_filepath}")

# Formats numbers cleanly with commas and 3 decimal places
def format_number(val: float, format_float: str = ",0.3f") -> str:
    try:
        val_float = float(val)
        # Check if it's practically an integer to avoid .000
        if val_float.is_integer():
            return f"{int(val_float):,}"
        return f"{val_float:{format_float}}"
    except ValueError:
        return str(val).replace('_', '\\_')

# Exports a DataFrame to LaTeX, detecting subheader rows with empty tail cells

# Exports a DataFrame to LaTeX with customizable header rows and columns
def generate_latex_from_generic(
    df: pd.DataFrame,
    filepath: str | Path,
    format_float: str = ",0.3f",
    rename_strat: dict[str, str] | None | str = None,
    hrows: int = 1,
    hcols: int = 1
) -> None:
    columns = list(df.columns)
    num_cols = len(columns)
    
    # Adjust alignment: 'l' for header columns, 'c' for data columns
    col_align = "l" * hcols + "c" * (num_cols - hcols)
    
    latex_lines = []
    latex_lines.append(f"\\begin{{tabular}}{{{col_align}}}")
    latex_lines.append("\t\\toprule\\toprule")
    
    # 1st Header row (DataFrame column names)
    header_titles = [str(c).replace('_', '\\_') for c in columns]
    header_clean = [h if "Unnamed" not in h else "~" for h in header_titles]
    latex_lines.append("\t" + " & ".join(header_clean) + " \\\\[0.8em]")
    
    # If there is only 1 header row, place the rule immediately
    if hrows == 1:
        latex_lines.append("\t\\midrule")
    
    row_counter = 0

    # Parameter rows
    for _, row in df.iterrows():
        val_first = row[columns[0]]
        first_not_blank = pd.notna(val_first) and str(val_first).strip() not in ("", "nan", "NaN", "None")
        
        rest_vals = [row[col] for col in columns[1:]]
        rest_all_blank = all(pd.isna(v) or str(v).strip() in ("", "nan", "NaN", "None") for v in rest_vals)
        
        # Subheader row logic
        if first_not_blank and rest_all_blank:
            subheader_text = str(val_first).replace('_', '\\_')
            latex_lines.append("\t\\addlinespace[0.8em]")
            latex_lines.append(f"\t\\multicolumn{{{num_cols}}}{{l}}{{\\itx{{{subheader_text}}}}} \\\\[0.4em]")
            latex_lines.append("\t\\hline")
            continue

        row_vals = []
        for i, col in enumerate(columns):
            val = row[col]
            # Print "~" for NaN or None values
            if pd.isna(val) or str(val).strip().lower() in ("nan", "none"):
                val = "~"
                row_vals.append(val)
                continue
            # Apply text logic to header columns, and numeric logic to data columns
            if i < hcols:
                format_latex_column(val, rename_strat)
                row_vals.append(val)
            else:
                # Iterate additional header rows without applying float formatting
                if row_counter < hrows - 1:
                    clean_val = str(val).replace('_', '\\_') if pd.notna(val) else "~"
                    row_vals.append(clean_val if clean_val.lower() not in ("nan", "none") else "~")
                else:
                    # Format actual numeric data
                    try:
                        row_vals.append(format_number(val, format_float))
                    except NameError:
                        row_vals.append(str(val))
        
        latex_lines.append("\t" + " & ".join(row_vals) + " \\\\[0.9em]")
        
        # Add hline once the final header row is printed
        if row_counter == hrows - 2:
            latex_lines.append("\t\\midrule")
            
        row_counter += 1
        
    latex_lines.append("\t\\bottomrule")
    latex_lines.append("\\end{tabular}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(latex_lines))
    
    print(f"Successfully exported df ({df.shape[0]:,}x{df.shape[1]:,}) to {filepath}")