import re
from pathlib import Path
import json

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

# Parses a .txt file containing linearmodels PanelOLS outputs
def parse_linear(filepath: str | Path) -> dict:
    lines = []
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
            models[current_model] = {
                'Y': '', 'params': {},
                'struct_params': [], 'instruments': [],
                'obs': '',
                'time_nb': '', 'entities_nb': '',
                'time_fe': False, 'entities_fe': False, 'network_fe': False,
                'r2-overall': '', 'r2': ''
            }
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
        elif 'R-squared (Overall):' in line:
            parts = line.split()
            models[current_model]['r2-overall'] = parts[-1]
        elif 'R-squared:' in line:
            parts = line.split()
            models[current_model]['r2'] = parts[-1]
        elif 'struct_map' in line or 'struct_calc' in line:
            line_val = (
                line
                .replace('struct_map: ', '')
                .replace('struct_calc: ', '')
                .strip()
                .replace('\'', '\"')
            )
            obj = json.loads(line_val) if line_val != '' else {}
            
            if isinstance(obj, dict):
                models[current_model]['struct_params'].extend(obj.values())
            elif isinstance(obj, list):
                models[current_model]['struct_params'].extend(obj)

        # Instruments line
        if 'Instruments:' in line:
            instr_str = line.split('Instruments:')[1].strip()
            instr_arr = instr_str.split(',') if instr_str else []
            models[current_model]['instruments'] = [v.strip() for v in instr_arr]
            continue

        # Test Results
        hansen_match = re.search(r'Hansen test.*Prob > Chi2\s*=\s*([\d\.]+)', line)
        if hansen_match:
            p_val = float(hansen_match.group(1))
            models[current_model]['hansen_p'] = f"{p_val:.3f}"
            models[current_model]['hansen_reject'] = p_val < 0.05

        # Extract parameters
        if 'Parameter Estimates' in line:
            in_params = True
            continue
            
        # Terminate on empty line (end of table) or F-test
        if in_params:
            if any([
                not line,
                line.startswith('F-test'),
                line.startswith('Endogenous:')
            ]):
                in_params = False
                continue


        if 'Included effects' in line:
            if 'Entity' in line:
                models[current_model]['entities_fe'] = True
            if 'Time' in line:
                models[current_model]['time_fe'] = True
            continue
        if 'fe: ' in line:
            if 't' in line:
                models[current_model]['time_fe'] = True
            if 'i' in line:
                models[current_model]['entities_fe'] = True
            if 'n' in line:
                models[current_model]['network_fe'] = True
            continue
            
        # Skip formatting dividers and table headers while inside the block
        if in_params and (line.startswith('===') or line.startswith('---') or line.startswith('Parameter')):
            continue
            
        if in_params:
            parts = line.split()
            if len(parts) >= 6:
                var_name = parts[0]
                coef = parts[1]
                se = parts[2]
                pval = parts[4]

                if not var_name or var_name.startswith('year_'):
                    continue
                
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