import ibis
from ibis import _
import traceback
import pandas as pd
import numpy as np
from dataclasses import dataclass, field, asdict

import statsmodels.api as sm
from linearmodels.panel import PanelOLS
from linearmodels.panel.results import PanelEffectsResults
from linearmodels.iv import IVGMMCUE
from linearmodels.iv.results import IVGMMResults

from panelbox.models.iv import PanelIV
from panelbox.core.results import PanelResults

from utils.f_0_dirs import get_data_dirs
dirs = get_data_dirs(segment="model")

use_linearmodels = True

@dataclass
class ModelSpec():
    Y: str
    X: list[str]
    W: list[str] = field(default_factory=list)
    Z: dict[str, list[str]] = field(default_factory=dict)
    to_log: list[str] = field(default_factory=list)
    fe: list[str] = field(default_factory=list)
    description: str = ""
    panel_name: str | None = None
    include: bool = True
    category: str | None = None
    use_linearmodels: bool = True
    differencing: str = 'mean'

def reindex_entity(df: pd.DataFrame) -> pd.DataFrame:
    min_year, max_year = df.index.get_level_values('year').min(), df.index.get_level_values('year').max()
    full_years = range(min_year, max_year + 1)
    full_idx = pd.MultiIndex.from_product([[df.index.get_level_values('registered_number').unique()[0]], full_years], names=['registered_number', 'year'])
    return df.reindex(full_idx)

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

def transform_nfe(values: list[str], fe: list[str]) -> list[str]:
    if 'lnfe' in fe:
        return [f"(i-wd1){'_' if len(p) == 1 else ''}{p}" for p in values]
    elif 'gnfe' in fe:
        return [f"(i-vd1){'_' if len(p) == 1 else ''}{p}" for p in values]
    else:
        return values

def run_panel(args: tuple[ModelSpec, pd.DataFrame | str, str]) -> tuple[PanelEffectsResults | PanelResults, str | dict[str, float], dict[str, pd.Series | None]]:
    mod, table_indicator, model_name = args

    try:

        # 1. Get the parameters for this regression
        params_raw = {
            "dep": [mod.Y],
            "regressors": mod.X + mod.W,
            "exog": [p for p in (mod.X + mod.W) if p not in mod.Z.keys()],
            "endog": [p for p in (mod.X + mod.W) if p in mod.Z.keys()],
            "instr": [p for values in mod.Z.values() for p in values]
        }
        params_raw_names = list({ prop: True for values in params_raw.values() for prop in transform_nfe(values, mod.fe) }.keys())
        params_transformed = {}
        for k, v in params_raw.items():
            values = transform_nfe(v, mod.fe)
            if k in mod.to_log:
                params_transformed[k] = [f'ln_{p}' for p in values]
            else:
                params_transformed[k] = values
        is_iv = len(params_transformed['endog']) > 0
        params_transformed_names = list({ prop: True for values in params_transformed.values() for prop in values }.keys())
        params_full = ['registered_number', 'year'] + params_transformed_names

        # 2. Get the data. We need to understand if it is a table or a DataFrame and get them both to a model form.
        if isinstance(table_indicator, str):
            con = ibis.duckdb.connect(dirs.db_path, read_only=True)
            t_model: ibis.Table = (
                con.table(table_indicator)
                .distinct(on=['registered_number', 'year'])
                .mutate(**{
                    f'ln_{p}': _[p].log() for p in params_raw_names if p in mod.to_log
                })
                .select(params_full)
                .drop_null(params_full)
            )
            df_model = pd.DataFrame()
        elif isinstance(table_indicator, pd.DataFrame):
            df_raw = table_indicator
            df_model: pd.DataFrame = (
                df_raw
                .drop_duplicates(subset=['registered_number', 'year'])
                .assign(**{
                    f'ln_{p}': df_raw[p].apply(lambda x: np.log(x) if x > 0 else None) for p in params_raw_names if p in mod.to_log
                })
                .filter(items=params_full)
                .dropna(subset=params_full)
            )
            t_model = ibis.memtable(df_model)
        else:
            raise ValueError(f"Invalid table_indicator type: {type(table_indicator)}. Must be str or pd.DataFrame.")

        # 3. Handle the regression based on whether it is IV or not.
        res: PanelEffectsResults | IVGMMResults | PanelResults | None = None
        if not is_iv:
            if df_model is None or df_model.empty:                                        # type: ignore
                df_model = t_model.execute()                            # type: ignore
            df_ols = df_model.set_index(['registered_number', 'year'])  # type: ignore

            print(f"Running model '{model_name}' as panel OLS")
            Y = df_ols[params_transformed['dep'][0]]
            X = sm.add_constant(df_ols[params_transformed['regressors']])
            
            # PanelOLS handles fixed effects
            mod_panel = PanelOLS(Y, X, entity_effects='i' in mod.fe, time_effects='t' in mod.fe)
            res_panel: PanelEffectsResults = mod_panel.fit(cov_type='clustered', cluster_entity=True)
            
            # Extract \beta results iterating through full_params
            effects_dict: dict[str, pd.Series | None] = {
                'i': res_panel.estimated_effects.xs('entity_effects', level=1) if 'entity_effects' in res_panel.estimated_effects.index.names else None,
                't': res_panel.estimated_effects.xs('time_effects', level=1) if 'time_effects' in res_panel.estimated_effects.index.names else None
            }
            res = res_panel

        elif mod.use_linearmodels:
            df_model = add_fe(t_model, mod.fe).execute()                          # type: ignore
            tdumm_cols = [col for col in df_model.columns if col.startswith('year_')]
            const_col = ['const'] if 'c' in mod.fe else []
            # Change the values of every value in the params_transformed dictionary
            # To have backticks around them, so that they can be used in the formula string
            params_ticked = {k: [f"`{p}`" for p in v] for k, v in params_transformed.items()}
            formula_str = "".join([

                            params_ticked['dep'][0],
                            ' ~ ',
                            ' + '.join(params_ticked['exog'] + tdumm_cols + const_col),
                            ' + [',
                            ' + '.join(params_ticked['endog']),
                            ' ~ ',
                            " + ".join(params_ticked['instr']),
                            ']'
                        ])
            print(f"Running model '{model_name}' as linearmodels panel IV, formula: {formula_str}")
            try:
                mod_iv = IVGMMCUE.from_formula(
                    formula=formula_str,
                    data=(df_model)
                )
                res_gmm: IVGMMResults = mod_iv.fit(cov_type='clustered', clusters=df_model['registered_number'])        # type: ignore
                # Extract \beta results, j-statistic, and first stage results
                if hasattr(res_gmm, 'j_stat') and res_gmm.j_stat is not None:       # type: ignore
                    print(f"J-statistic (rej if overidentified): {res_gmm.j_stat.stat:.2f}, p-value: {res_gmm.j_stat.pval:.3f}")
                effects_dict: dict[str, pd.Series | None] = { 'i': None, 't': None }
                res = res_gmm
            except Exception as e:
                with pd.ExcelWriter(dirs.tmp_dir / f"error_{model_name}.xlsx") as writer:
                    df_model.to_excel(writer, sheet_name='model_data', index=False)
                print(f"Wrote model data to {dirs.tmp_dir / f'error_{model_name}.xlsx'} for debugging.")
                raise e

        else:
            df_model = t_model.execute()    # type: ignore
            params_ticked = {k: [f"`{p}`" for p in v] for k, v in params_transformed.items()}
            formula_str = "".join([
                params_ticked['dep'][0],
                ' ~ ',
                ' + '.join(params_ticked['regressors']),
                ' | ',
                ' + '.join(params_ticked['exog'] + params_ticked['instr'])
            ])
            print(f"Running model '{model_name}' as PanelBox panel IV, formula: {formula_str}")
            mod_iv = PanelIV(
                formula=formula_str,
                data=df_model,
                entity_col='registered_number',
                time_col='year',
                model_type=(
                    'fe' if 'i' in mod.fe and 't' in mod.fe else
                    're' if 'i' not in mod.fe and 't' not in mod.fe else
                    'pooled'
                )
            )
            res_ivpbox: PanelResults = mod_iv.fit(cov_type='clustered', cluster_entity=True)
            try:
                effects_dict = { 'i': None, 't': None }
                if res_ivpbox.first_stage_results is not None:
                    for var, fs in res_ivpbox.first_stage_results.items():
                        print(f"{var}: F-stat = {fs['f_statistic']:.2f}")
            except Exception as e:
                print(f"Warning: Could not extract first stage results. {type(e).__name__}: {e}")
                traceback.print_exc()  # Print the full traceback for debugging
            res = res_ivpbox

        beta: dict[str, float] = { p: res.params[p] for p in params_transformed['regressors'] }
        print(f"✅ Model '{model_name}' estimated: {", ".join([f'{k}={v:.3f}' for k, v in beta.items()])}")
        return res, beta, effects_dict  # type: ignore
    
    except Exception as e:
        print(f"❌ Model '{model_name}' failed. {type(e).__name__}: {e}")
        traceback.print_exc()  # Print the full traceback for debugging
        with open(dirs.output_dir / "error.log", "a") as f:
            f.write(f"Model '{model_name}' failed. {type(e).__name__}: {e}\n")
            traceback.print_exc(file=f)
        return None, None, None     #type: ignore

def format_str(res_serie: tuple[PanelEffectsResults | IVGMMResults, ModelSpec, str]) -> str:
    res, mod, model_name = res_serie
    
    # 5. Store the results and parameters
    param_str = ""
    param_str += "Model Parameters:\n"
    for key, value in asdict(mod).items():
        if isinstance(value, list) and len(value) == 0:
            continue
        if value is None:
            continue
        param_str += f"{key}: {value}\n"

    output_str = ""
    output_str += f"Model '{model_name}': {mod.description}\n"
    output_str += param_str + "\n"
    output_str += f"{res.summary}\n\n"
    output_str += "=" * 87 + "\n\n"
    if hasattr(res, 'j_stat') and res.j_stat is not None:       # type: ignore
        output_str += "Hansen J-statistic:\n"
        output_str += res.j_stat.__str__()                      # type: ignore
        output_str += '\n'

    return output_str