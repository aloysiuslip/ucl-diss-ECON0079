import ibis
from ibis import _
import traceback
import pandas as pd
import numpy as np
from dataclasses import dataclass, field, asdict

import statsmodels.api as sm
from linearmodels.panel import PanelOLS
from linearmodels.panel.results import PanelEffectsResults

from panelbox.models.iv import PanelIV
from panelbox.core.results import PanelResults

from utils.f_0_dirs import get_data_dirs
dirs = get_data_dirs(segment="model")

@dataclass
class ModelSpec():
    Y: str
    X: list[str]
    W: list[str] = field(default_factory=list)
    Z: dict[str, list[str]] = field(default_factory=dict)
    to_log: list[str] = field(default_factory=list)
    fe: list[str] = field(default_factory=list)
    description: str = ""
    include: bool = True

def run_panel(args: tuple[ModelSpec, pd.DataFrame | str, str]) -> tuple[PanelEffectsResults | PanelResults, str | dict[str, float], dict[str, pd.Series | None]]:
    mod, table_indicator, model_name = args
    try:

        params_raw = {
            "dep": [mod.Y],
            "regressors": mod.X + mod.W,
            "exog": [p for p in (mod.X + mod.W) if p not in mod.Z.keys()],
            "endog": [p for p in (mod.X + mod.W) if p in mod.Z.keys()],
            "instr": [p for values in mod.Z.values() for p in values]
        }
        params_raw_names = list({ prop: True for values in params_raw.values() for prop in values }.keys())
        params_transformed = {}
        for k, v in params_raw.items():
            if k in mod.to_log:
                params_transformed[k] = [f'ln_{p}' for p in v]
            else:
                params_transformed[k] = v
        is_iv = len(params_transformed['endog']) > 0
        params_transformed_names = list({ prop: True for values in params_transformed.values() for prop in values }.keys())
        params_full = ['registered_number', 'year'] + params_transformed_names

        # 1. Execute into a Pandas DataFrame and set the MultiIndex for linearmodels
        if isinstance(table_indicator, str):
            con = ibis.duckdb.connect(dirs.db_path, read_only=True)
            t_panel: ibis.Table = con.table(table_indicator)
            df_model: pd.DataFrame = (
                t_panel
                .distinct(on=['registered_number', 'year'])
                .mutate(**{
                    f'ln_{p}': _[p].log() for p in params_raw_names if p in mod.to_log
                })
                .drop_null(params_full)
                .select(params_full)
                .execute()
                .set_index(['registered_number', 'year'])
            )
        elif isinstance(table_indicator, pd.DataFrame):
            df_raw = table_indicator
            df_model: pd.DataFrame = (
                df_raw
                .drop_duplicates(subset=['registered_number', 'year'])
                .assign(**{
                    f'ln_{p}': df_raw[p].apply(lambda x: np.log(x) if x > 0 else None) for p in params_raw_names if p in mod.to_log
                })
                .dropna(subset=params_full)
                .filter(items=params_full)
            )
        else:
            raise ValueError(f"Invalid table_indicator type: {type(table_indicator)}. Must be str or pd.DataFrame.")

        if not is_iv:
            df_ols = df_model.set_index(['registered_number', 'year'])
            print(f"Running model '{model_name}' as panel OLS")
            Y = df_ols[params_transformed['dep'][0]]
            X = sm.add_constant(df_ols[params_transformed['regressors']])
            
            # 2. Estimate the model with Firm and Year Fixed Effects
            mod_panel = PanelOLS(Y, X, entity_effects='i' in mod.fe, time_effects='t' in mod.fe)
            res = mod_panel.fit(cov_type='clustered', cluster_entity=True)
            
            # Extract \beta results iterating through full_params
            effects_dict: dict[str, pd.Series | None] = {
                'i': res.estimated_effects.xs('entity_effects', level=1) if 'entity_effects' in res.estimated_effects.index.names else None,
                't': res.estimated_effects.xs('time_effects', level=1) if 'time_effects' in res.estimated_effects.index.names else None
            }
        else:

            print(df_model.columns)
            formula_str = "".join([
                params_transformed['dep'][0],
                ' ~ ',
                ' + '.join(params_transformed['regressors']),
                ' | ',
                ' + '.join(params_transformed['exog'] + params_transformed['instr'])
            ])
            print(f"Running model '{model_name}' as panel IV, formula: {formula_str}")
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
            res = mod_iv.fit(cov_type='clustered')
            effects_dict = { 'i': None, 't': None }
            if res.first_stage_results is not None:
                for var, fs in res.first_stage_results.items():
                    print(f"{var}: F-stat = {fs.f_stat:.3f}, p-value = {fs.pval:.3f}")

        beta: dict[str, float] = { p: res.params[p] for p in params_transformed['regressors'] }

        print(f"✅ Model '{model_name}' estimated: {", ".join([f'{k}={v:.3f}' for k, v in beta.items()])}")
        return res, beta, effects_dict
    
    except Exception as e:
        print(f"❌ Model '{model_name}' failed. {type(e).__name__}: {e}")
        traceback.print_exc()  # Print the full traceback for debugging
        with open(dirs.output_dir / "error.log", "a") as f:
            f.write(f"Model '{model_name}' failed. {type(e).__name__}: {e}\n")
            traceback.print_exc(file=f)
        return None, None, None     #type: ignore

def format_str(res_serie: tuple[PanelEffectsResults, ModelSpec, str]) -> str:
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

    return output_str