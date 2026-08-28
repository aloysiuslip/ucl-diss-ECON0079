import re
import pandas as pd
from pathlib import Path

# Helper to convert a p-value string into significance stars.
def get_stars(p_val_str: str) -> str:
    try:
        p_val = float(p_val_str)
        if p_val < 0.01:
            return "***"
        elif p_val < 0.05:
            return "**"
        elif p_val < 0.1:
            return "*"
    except ValueError:
        pass
    return ""

# Formats parameter names for LaTeX with subscripts and text italics
def format_param(param: str) -> str:
    if param == 'const':
        return 'constant'

    d: dict[str, str] = {'core': param}
    
    if 'ln_' in param:
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
    return final_str.replace('_', '\\_')

# Generates the \lblock or \cblock LaTeX macros for the table
def form_block(args: tuple[str | None, str | None] | None = None, block_type: str = 'l', size: tuple[str | None, str | None] = (None, None)) -> str:
    
    param_str, value_str = args if args else (None, None)
    if not param_str:
        param_str = '~'
    if not value_str:
        value_str = '~'
    if size[0]:
        param_str = f"\\{size[0]}{{{param_str}}}"
    if size[1]:
        value_str = f"\\{size[1]}{{{value_str}}}"
    return (
        f"\t\t\\{block_type}block{{\n"
        f"\t\t\t{param_str}\n"
        f"\t\t\t\\\\\n"
        f"\t\t\t{value_str}\n"
        f"\t\t}}"
    )

# Parses a .txt file containing linearmodels PanelOLS outputs
def parse_linearmodels_txt(filepath: str | Path) -> dict:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    models = {}
    current_model = None
    in_params = False

    for line in lines:
        line = line.strip()
        
        # Detect model header
        model_match = re.search(r"Model '([^']+)':", line)
        if model_match:
            current_model = model_match.group(1)
            models[current_model] = {'Y': '', 'params': {}, 'obs': '',
                                     'time_nb': '', 'entities_nb': '',
                                     'time_fe': False, 'entities_fe': False, 'r2': ''}
            in_params = False
            continue
            
        if not current_model:
            continue
            
        # Extract metadata
        if line.startswith('Y:'):
            models[current_model]['Y'] = line.split(':')[1].strip()
        elif 'No. Observations:' in line:
            parts = line.split()
            idx = parts.index('Observations:')
            models[current_model]['obs'] = f"{int(parts[idx+1]):,}"
        elif 'Entities:' in line:
            models[current_model]['entities_nb'] = f"{int(line.split()[1]):,}"
        elif 'Time periods:' in line:
            models[current_model]['time_nb'] = f"{int(line.split()[2]):,}"
        elif 'R-squared (Within):' in line or 'R-squared:' in line:
            parts = line.split()
            models[current_model]['r2'] = parts[-1]

        # Extract parameters
        if 'Parameter Estimates' in line:
            in_params = True
            continue
            
        # FIXED: Terminate on empty line (end of table) or F-test
        if in_params and (not line or line.startswith('F-test')):
            in_params = False
            continue

        if 'Included effects' in line:
            if 'Entity' in line:
                models[current_model]['entities_fe'] = True
            if 'Time' in line:
                models[current_model]['time_fe'] = True
            continue
            
        # FIXED: Skip formatting dividers and table headers while inside the block
        if in_params and (line.startswith('===') or line.startswith('---') or line.startswith('Parameter')):
            continue
            
        if in_params:
            parts = line.split()
            if len(parts) >= 6:
                var_name = parts[0]
                coef = parts[1]
                se = parts[2]
                pval = parts[4]
                
                if var_name == '_con':
                    var_name = 'const'
                
                try:
                    coef_fmt = f"{float(coef):.3f}"
                    se_fmt = f"{float(se):.3f}"
                except ValueError:
                    coef_fmt = coef
                    se_fmt = se

                models[current_model]['params'][var_name] = {
                    'coef': coef_fmt,
                    'se': se_fmt,
                    'stars': get_stars(pval)
                }
                
    return models

# Parses a .txt file containing pydynpd outputs."""
def parse_pydynpd_txt(filepath: str | Path) -> dict:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    models = {}
    current_model = None
    model_count = 0

    for line in lines:
        line = line.strip()
        
        if 'Generated Command String:' in line:
            model_count += 1
            current_model = f"dyn{model_count}"
            models[current_model] = {
                'Y': '', 'params': {}, 'obs': '', 'entities_fe': True, 'time_fe': False,
                'hansen_stat': '', 'hansen_p': '', 'hansen_reject': None,
                'ar1_stat': '', 'ar1_p': '', 'ar1_reject': None,
                'ar2_stat': '', 'ar2_p': '', 'ar2_reject': None
            }
            continue
            
        if not current_model:
            continue
            
        # Summary Statistics
        obs_match = re.search(r'Number of obs\s*=\s*(\d+)', line)
        if obs_match:
            models[current_model]['obs'] = f"{int(obs_match.group(1)):,}"
            
        if 'timedumm' in line:
            models[current_model]['time_fe'] = True
            continue

        # Test Results
        hansen_match = re.search(r'Hansen test.*Prob > Chi2\s*=\s*([\d\.]+)', line)
        if hansen_match:
            p_val = float(hansen_match.group(1))
            models[current_model]['hansen_p'] = f"{p_val:.3f}"
            models[current_model]['hansen_reject'] = p_val < 0.05

        ar1_match = re.search(r'AR\(1\).*Pr > z\s*=\s*([\d\.]+)', line)
        if ar1_match:
            p_val = float(ar1_match.group(1))
            models[current_model]['ar1_p'] = f"{p_val:.3f}"
            models[current_model]['ar1_reject'] = p_val < 0.05

        ar2_match = re.search(r'AR\(2\).*Pr > z\s*=\s*([\d\.]+)', line)
        if ar2_match:
            p_val = float(ar2_match.group(1))
            models[current_model]['ar2_p'] = f"{p_val:.3f}"
            models[current_model]['ar2_reject'] = p_val < 0.05

        # Parameter Table[cite: 1]
        if line.startswith('|'):
            if 'coef.' in line:
                models[current_model]['Y'] = line.split('|')[1].strip()
                continue
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 7:
                var_name = parts[1]
                if not var_name or var_name.startswith('year_'):
                    continue
                if var_name == '_con':
                    var_name = 'const'
                    
                coef, se, stars = parts[2], parts[3], parts[6]
                try:
                    models[current_model]['params'][var_name] = {
                        'coef': f"{float(coef):.3f}", 
                        'se': f"{float(se):.3f}", 
                        'stars': stars
                    }
                except ValueError:
                    models[current_model]['params'][var_name] = {'coef': coef, 'se': se, 'stars': stars}

    return models

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
    return form_block((symbol, f"({p_val}){star_str}"), block_type='c', size=(None, 'footnotesize'))

# Combines models into a final .tex table.
def generate_latex_table(models: dict, output_filepath: str | Path, show: list[int] | None = None) -> None:

    # If the show parameter is provided, filter the models to only include those indices
    if show is not None:
        model_names = list(models.keys())
        filtered_m_names = [model_names[i - 1] for i in show]
        filtered_models = {name: models[name] for name in filtered_m_names}
        models = filtered_models

    model_names = list(models.keys())
    unique_params = set()
    for mod in models.values():
        unique_params.update(mod['params'].keys())
        
    sorted_params = sorted(list(unique_params), key=lambda x: (x != 'const', x))

    latex_lines = [f"\t\\begin{{tabular}}{{l{'c' * len(model_names)}}}"]
    
    # Header row
    cols = [form_block()]
    for i, mod in enumerate(model_names):
        y_str = format_param(models[mod].get('Y', 'Y'))
        cols.append(form_block((f"({i + 1})", y_str), block_type='c', size=('footnotesize', 'small')))
    latex_lines.extend(["\t\t\\toprule\\toprule", " & ".join(cols) + " \\\\[0.8em]", "\t\t\\toprule"])

    # Coefficients
    for param in sorted_params:
        row_lines = [form_block((format_param(param), '~'))]
        for mod in model_names:
            mod_data = models[mod]['params'].get(param)
            if mod_data:
                cblock = form_block((f"${mod_data['coef']}$", f"({mod_data['se']}){mod_data['stars']}"), block_type='c', size=(None, 'footnotesize'))
                row_lines.append(cblock)
            else:
                row_lines.append(" ")
        latex_lines.extend([" & ".join(row_lines), "\t\t\\\\ [0.9em]"])

    # Summary and Test Statistics
    latex_lines.append("\t\t\\hline")
    
    # Handle GMM Test rows if they exist in the model dictionary
    has_gmm_tests = any('hansen_p' in m and m['hansen_p'] for m in models.values())
    if has_gmm_tests:
        for test_key, test_name in [('hansen', 'Hansen Test'), ('ar1', 'AR(1) Test'), ('ar2', 'AR(2) Test')]:
            cells = [build_test_cblock(models[m].get(f'{test_key}_reject'), models[m].get(f'{test_key}_p', '')) for m in model_names]
            latex_lines.append(f"\t\t{form_block((test_name, None))} & " + " & ".join(cells) + "\n\t\t\\\\ [0.9em]")
        latex_lines.append("\t\t\\hline")

    # Observations, time, entities
    i_row = "\t\t\\textit{i} fixed effects & " + " & ".join([build_fe(models[m].get('entities_fe')) for m in model_names]) + "\n\t\t\\\\"
    t_row = "\t\t\\textit{t} fixed effects & " + " & ".join([build_fe(models[m].get('time_fe')) for m in model_names]) + "\n\t\t\\\\"
    obs_row = "\t\tObservations & " + " & ".join([models[m].get('obs') for m in model_names]) + "\n\t\t\\\\"
    # Only add the i_row if there is at least one model with a non-empty entities_fe
    if any(models[m].get('entities_fe') for m in model_names):
        latex_lines.append(i_row)
    if any(models[m].get('time_fe') for m in model_names):
        latex_lines.append(t_row)
    if any(models[m].get('obs') for m in model_names):
        latex_lines.append(obs_row)
    
    # Handle R-squared if it exists (for standard OLS models)
    has_r2 = any('r2' in m and m['r2'] for m in models.values())
    if has_r2:
        r2_row = "\t\tR$^2$ & " + " & ".join([models[m].get('r2', '') for m in model_names]) + "\n\t\t\\\\"
        latex_lines.append(r2_row)

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
    
def generate_latex_from_generic(df: pd.DataFrame, filepath: str, format_float: str = ",0.3f") -> None:
    columns = list(df.columns)
    col_align = "l" + "c" * (len(columns) - 1)
    
    latex_lines = []
    latex_lines.append(f"\\begin{{tabular}}{{{col_align}}}")
    latex_lines.append("\t\\toprule\\toprule")
    
    # Header row
    header_clean = [str(c).replace('_', '\\_') for c in columns]
    latex_lines.append("\t" + " & ".join(header_clean) + " \\\\[0.8em]")
    latex_lines.append("\t\\toprule")
    
    # Parameter rows
    for _, row in df.iterrows():
        row_vals = []
        for i, col in enumerate(columns):
            val = row[col]
            if i == 0:
                row_vals.append(format_param(str(val)))
            else:
                row_vals.append(format_number(val, format_float))
        
        latex_lines.append("\t" + " & ".join(row_vals) + " \\\\[0.9em]")
        
    latex_lines.append("\t\\bottomrule")
    latex_lines.append("\\end{tabular}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("\n".join(latex_lines))
    
    print(f"Successfully exported df ({df.shape[0]:,}x{df.shape[1]:,}) to {filepath}")