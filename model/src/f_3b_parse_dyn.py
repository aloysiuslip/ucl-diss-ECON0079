import re
from pathlib import Path
import json

# Parses a .txt file containing pydynpd outputs."""
def parse_dyn(filepath: str | Path) -> dict:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    models = {}
    current_model = None
    model_count = 0

    for line in lines:
        line = line.strip()
        
        if 'Dynamic panel-data estimation' in line:
            model_count += 1
            current_model = f"dyn{model_count}"
            models[current_model] = {
                'Y': '', 'params': {}, 'obs': '',
                'struct_params': [],
                'instruments': [],  
                'entities_fe': True, 'time_fe': False, 'network_fe': False,
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

        # obs_match = re.search(r'Number of instruments\s*=\s*(\d+)', line)
        # if obs_match:
        #     models[current_model]['instruments'] = f"{int(obs_match.group(1)):,}"
            
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

        if 'struct_map' in line or 'struct_calc' in line:
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

        if 'instruments:' in line:
            line_val = (
                line
                .replace('instruments:', '')
                .strip()
                .replace('\'', '\"')
            )
            obj = json.loads(line_val) if line_val != '' else {}
            if isinstance(obj, list):
                models[current_model]['instruments'].extend(obj)

        # Parameter Table
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