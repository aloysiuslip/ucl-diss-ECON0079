
import numpy as np
from rpds import List
from scipy import stats
from linearmodels.iv.results import IVGMMResults
from dataclasses import dataclass, field, asdict

@dataclass
class ModelSpec():
    Y: str
    X: list[str]
    W: list[str] = field(default_factory=list)
    Z: dict[str, list[str]] = field(default_factory=dict)
    to_log: list[str] = field(default_factory=list)
    fe: list[str] = field(default_factory=list)
    fe_type: str = 'd'
    description: str = ""
    panel_name: str | None = None
    include: bool = True
    category: str | None = None
    differencing: str = 'mean'

    # Model options
    use_linearmodels: bool = True
    run_ols_test: bool = False

    # Structural params map
    struct_map: dict[str, str] = field(default_factory=dict)
    struct_calc: list[str] | None = None

def extract_structural(res: IVGMMResults, mod: ModelSpec) -> dict[str, tuple[float, float]]:

    structural_out_dict = {}
    alpha = 0.05
    display_names = ("SE", "t-stat", "p-value", "Lower CI", "Upper CI")

    struct_calc = mod.struct_calc if mod.struct_calc is not None else ['xi_0', 'zeta_0']
    delta_0_name = None

    # Easy handling: these are exactly listed, just rename them
    for red_name, struct_name in mod.struct_map.items():
        if red_name not in res.params.index:
            continue
        coef = res.params[red_name]
        se = np.sqrt(res.cov.loc[red_name, red_name]) # type: ignore
        t_stat = coef / se
        p_val = 2 * (1 - stats.t.cdf(np.abs(t_stat), df=res.nobs - len(res.params)))
        crit_val = stats.t.ppf(1 - alpha / 2, df=res.nobs - len(res.params))
        if has_attr(res, 'table'):
            table_row: dict[str, float] = res.table.loc[red_name]     # type: ignore
            se = table_row['std_err']
            t_stat = table_row['z_value']
            p_val = table_row['p_value']
        lower_ci = coef - crit_val * se
        upper_ci = coef + crit_val * se

        structural_out_dict[struct_name] = (coef, se, t_stat, p_val, lower_ci, upper_ci)
        out_str = f"{struct_name}: {coef:.4f}"
        out_str += ",".join([f"{label}: {value:.4f}" for label, value in zip(display_names, list(structural_out_dict[struct_name][1:]))])
        if struct_name == 'delta_0':
            delta_0_name = red_name
        print(out_str)

    # These are non-linear mappings that require calculation
    inbuilt_structur_red = {
        'xi_1': { 'name_wxs': ['wg1_k'], 'name_beta': 'k'},
        'zeta_1': { 'name_wxs': ['wg1_l'], 'name_beta': 'l'},
        'xi_2': { 'name_wxs': ['wg2_k'], 'name_beta': 'k'},
        'zeta_2': { 'name_wxs': ['wg2_l'], 'name_beta': 'l'},
        'xi_3': { 'name_wxs': ['wg3_k'], 'name_beta': 'k'},
        'zeta_3': { 'name_wxs': ['wg3_l'], 'name_beta': 'l'},
        'xi_0': { 'name_wxs': ['wg1_k', 'wd1_k', 'wd2_k', 'wd3_k'], 'name_beta': 'k'},
        'zeta_0': { 'name_wxs': ['wg1_l', 'wd1_l', 'wd2_l', 'wd3_l'], 'name_beta': 'l'}
    }
    valid_params = []
    if isinstance(struct_calc, list):
        valid_params = [param for param in struct_calc if param in inbuilt_structur_red]
    elif isinstance(struct_calc, dict):
        valid_params = struct_calc.keys()
    else:
        print(f"✅ Structural parameters extracted: {', '.join(structural_out_dict.keys())}. No calculations")
        return structural_out_dict

    for param in valid_params:
        if isinstance(struct_calc, list):
            struct_info = inbuilt_structur_red[param]
        else:
            struct_info = struct_calc[param]

        name_wx_arr = [wx for wx in struct_info['name_wxs'] if wx in res.params.index]
        if len(name_wx_arr) == 0:
            print(f"Warning: calculating structural parameter '{param}', could not find any of {struct_info['name_wxs']} in model parameters. Skipping.")
            continue
        else:
            name_wx = name_wx_arr[0] 
        x = struct_info['name_beta']
        delta_0_val = 'delta_' + param.split('_')[1] if len(param.split('_')) > 1 else None
        delta_0_name_arr = [k for k,v in mod.struct_map.items() if v == delta_0_val]
        if len(delta_0_name_arr) == 0 or delta_0_name_arr[0] not in res.params.index:
            print(f"Warning: calculating structural parameter '{param}', could not find '{delta_0_val}' in the structural map. Skipping.")
            continue
        else:
            delta_0_name = delta_0_name_arr[0]
        coef_wx = res.params[name_wx]
        beta = res.params[x]
        delta_0 = res.params[delta_0_name]

        # Mean
        structural_xi = coef_wx + (beta * delta_0)

        # Variance: Delta method
        gradient = np.array([1, delta_0, beta])
        vars_of_interest = [name_wx, x, delta_0_name]
        var_cov_matrix = res.cov.loc[vars_of_interest, vars_of_interest].values
        structural_variance = gradient.T @ var_cov_matrix @ gradient
        structural_se = np.sqrt(structural_variance)
        structural_t_stat = structural_xi / structural_se
        structural_p_val = 2 * (1 - stats.t.cdf(np.abs(structural_t_stat), df=res.nobs - len(res.params)))
        crit_val = stats.t.ppf(1 - alpha / 2, df=res.nobs - len(res.params))
        lower_ci = structural_xi - crit_val * structural_se
        upper_ci = structural_xi + crit_val * structural_se

        structural_out_dict[param] = (structural_xi, structural_se, structural_t_stat, structural_p_val, lower_ci, upper_ci)
        out_str = f"{param}: {structural_xi:.4f}"
        out_str += ", ".join([f"{label}: {value:.4f}" for label, value in zip(display_names, list(structural_out_dict[param][1:]))])
        print(out_str)

    print(f"✅ Structural parameters extracted: {', '.join(structural_out_dict.keys())}")

    return structural_out_dict