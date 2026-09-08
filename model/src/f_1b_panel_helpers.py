import ibis
from ibis import _
import pandas as pd
import numpy as np

from scipy import stats
from linearmodels.iv.results import IVGMMResults

from utils.f_0_dirs import get_data_dirs
from f_1a_run_panel import ModelSpec
dirs = get_data_dirs(segment="model")

def reindex_entity(df: pd.DataFrame) -> pd.DataFrame:
    min_year, max_year = df.index.get_level_values('year').min(), df.index.get_level_values('year').max()
    full_years = range(min_year, max_year + 1)
    full_idx = pd.MultiIndex.from_product([[df.index.get_level_values('registered_number').unique()[0]], full_years], names=['registered_number', 'year'])
    return df.reindex(full_idx)

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
    for param in struct_calc:
        if param not in inbuilt_structur_red:
            print(f"Severe warning: Structural parameter '{param}' is not in the output dictionary. Skipping.")
            continue
        struct_info = inbuilt_structur_red[param]

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

def add_fe(table_indicator: ibis.Table | pd.DataFrame, fe: list[str]) -> ibis.Table:

    if isinstance(table_indicator, pd.DataFrame):
        t_panel = ibis.memtable(table_indicator)
    else:
        t_panel = table_indicator

    if 't' in fe:
        t_panel_tdumm = (
            t_panel
            .mutate(
                t_val=ibis.literal(1, type="int64"),
                year_clone=_.year.cast("string")
            )
            .pivot_wider(
                names_from='year_clone',
                values_from='t_val',
                names_prefix='year',
                values_fill=ibis.literal(0, type="int64")
            )
        )
        t_panel = t_panel_tdumm

    if 'i' in fe:
        diff_exprs = {}
        numeric_cols = [
            col for col, dtype in t_panel.schema().items() 
            if dtype.is_numeric() and col not in ['registered_number', 'year']
        ]
        w = ibis.window(group_by="registered_number", order_by="year")
        for col in numeric_cols:
            diff_exprs[col] = ibis.ifelse(

                # CONDITION: Is the previous row exactly one year ago?
                _.year == _.year.lag(1).over(w) + 1,

                # TRUE: Calculate the first difference
                _[col] - _[col].lag(1).over(w),
                
                # FALSE: Force a NULL (safe fallback for gaps and first-years)
                ibis.literal(None, type="float64")
            )
        t_panel_1diff = t_panel.mutate(**diff_exprs)
        if 't' in fe:
            min_year = t_panel['year'].min().execute()
            null_col = f'year_{min_year}'
            t_panel_filtered = t_panel_1diff.filter(_.year > min_year)
            if null_col in t_panel_filtered.columns:
                t_panel_filtered = t_panel_filtered.drop(null_col)
            t_panel = t_panel_filtered
        else:
            t_panel = t_panel_1diff

    if 'c' in fe:
        t_panel = t_panel.mutate(
            const=ibis.literal(1, type="int64")
        )
    t_panel_final_filter = t_panel.drop_null(how='any')
    return t_panel_final_filter


def transform_nfe(values: list[str], fe: list[str], fe_type: str) -> list[str]:
    if 'lnfe' in fe:
        return [f"(i-w{fe_type}1){'_' if len(p) == 1 else ''}{p}" for p in values]
    elif 'gnfe' in fe:
        return [f"(i-v{fe_type}1){'_' if len(p) == 1 else ''}{p}" for p in values]
    else:
        return values