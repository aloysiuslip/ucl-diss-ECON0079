import ibis
from ibis import _
import traceback
import pandas as pd
import numpy as np
from dataclasses import dataclass, field, asdict

from utils.f_0_dirs import get_data_dirs

import statsmodels.api as sm
from linearmodels.panel import PanelOLS
from linearmodels.panel.results import PanelEffectsResults

dirs = get_data_dirs(segment="model")

@dataclass
class ModelSpec():
    Y: str
    X: list[str]
    W: list[str] = field(default_factory=list)
    to_log: list[str] = field(default_factory=list)
    fe: list[str] = field(default_factory=list)
    description: str = ""
    include: bool = True

def run_panel(args: tuple[ModelSpec, pd.DataFrame, str]) -> tuple[PanelEffectsResults, str | dict[str, float], dict[str, pd.Series | None]]:
    mod, table_indicator, model_name = args
    print(f"Running model '{model_name}'")
    try:

        params_named = [mod.Y] + mod.X + mod.W
        params_named_full = ['registered_number', 'year'] + params_named
        if 'Y' in mod.to_log:
            mod.to_log.append(mod.Y)
        if 'X' in mod.to_log:
            mod.to_log.extend(mod.X)
        if 'W' in mod.to_log:
            mod.to_log.extend(mod.W)
        should_log_Y = mod.Y in mod.to_log
        param_Y = f'ln_{mod.Y}' if should_log_Y else mod.Y
        params_transformed = [f'ln_{p}' if p in mod.to_log else p for p in params_named]
        params_regressors = [p for p in params_transformed if p != param_Y]
        params_full = ['registered_number', 'year'] + params_transformed
        # 1. Execute into a Pandas DataFrame and set the MultiIndex for linearmodels
        if isinstance(table_indicator, str):
            con = ibis.duckdb.connect(dirs.db_path, read_only=True)
            t_panel: ibis.Table = con.table(table_indicator, read_only=True)
            df_model = (
                t_panel
                .select(['registered_number', 'year'] + params_named)
                .mutate(**{
                    f'ln_{p}': _[p].log() for p in params_full for p in params_named if p in mod.to_log
                })
                .drop_null(params_full)
                .select(params_full)
                .execute()
                .set_index(['registered_number', 'year'])
            )
        elif isinstance(table_indicator, pd.DataFrame):
            df_raw = table_indicator
            df_model = (
                df_raw
                .filter(items=params_named_full)
                .assign(**{
                    f'ln_{p}': df_raw[p].apply(lambda x: np.log(x) if x > 0 else None) for p in params_named if p in mod.to_log
                })
                .dropna(subset=params_full)
                .filter(items=params_full)
                .set_index(['registered_number', 'year'])
            )
        else:
            raise ValueError(f"Invalid table_indicator type: {type(table_indicator)}. Must be str or pd.DataFrame.")
        
        Y = df_model[param_Y]
        X = sm.add_constant(df_model[list(params_regressors)])
        
        # 2. Estimate the model with Firm and Year Fixed Effects
        mod_panel = PanelOLS(Y, X, entity_effects='i' in mod.fe, time_effects='t' in mod.fe)
        res = mod_panel.fit(cov_type='clustered', cluster_entity=True)
        
        # Extract \beta results iterating through full_params
        beta: dict[str, float] = { p: res.params[p] for p in params_regressors }
        effects_dict: dict[str, pd.Series | None] = {
            'i': res.estimated_effects.xs('entity_effects', level=1) if 'entity_effects' in res.estimated_effects.index.names else None,
            't': res.estimated_effects.xs('time_effects', level=1) if 'time_effects' in res.estimated_effects.index.names else None
        }

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