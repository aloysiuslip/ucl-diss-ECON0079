import ibis
from ibis import _
import traceback
import pandas as pd
import numpy as np
from dataclasses import dataclass, field, asdict

import statsmodels.api as sm
from linearmodels import OLS
from linearmodels.panel import PanelOLS
from linearmodels.panel.results import PanelEffectsResults
from linearmodels.iv import IVGMMCUE
from linearmodels.iv.results import IVGMMResults, OLSResults

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

from model.src.f_1b_panel_helpers import add_fe, transform_nfe, extract_structural

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
        params_raw_names = list({ prop: True for values in params_raw.values() for prop in transform_nfe(values, mod.fe, mod.fe_type) }.keys())
        params_transformed = {}
        for k, v in params_raw.items():
            values = transform_nfe(v, mod.fe, mod.fe_type)
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
            object.__setattr__(res_panel, 'structural_params', extract_structural(res_panel, mod))
            effects_dict: dict[str, pd.Series | None] = {
                'i': res_panel.estimated_effects.xs('entity_effects', level=1) if 'entity_effects' in res_panel.estimated_effects.index.names else None,
                't': res_panel.estimated_effects.xs('time_effects', level=1) if 'time_effects' in res_panel.estimated_effects.index.names else None
            }
            res = res_panel

        # IV model, but we run an endogenous OLS test first to see R^2
        elif mod.run_ols_test:
            df_model = add_fe(t_model, mod.fe).execute()                          # type: ignore
            tdumm_cols = [col for col in df_model.columns if col.startswith('year_')]
            const_col = ['const'] if 'c' in mod.fe else []
            params_ticked = {k: [f"`{p}`" for p in v] for k, v in params_transformed.items()}
            formula_str = "".join([
                            params_ticked['dep'][0],
                            ' ~ ',
                            ' + '.join(params_ticked['exog'] + tdumm_cols + const_col),
                            ' + ',
                            ' + '.join(params_ticked['endog'])
                        ])
            print(f"Running model '{model_name}' as linearmodels panel endogenous OLS, formula: {formula_str}")
            try:
                mod_ols = OLS.from_formula(
                    formula=formula_str,
                    data=(df_model)
                )
                res_ols: OLSResults = mod_ols.fit(cov_type='clustered', clusters=df_model['registered_number'])
                effects_dict: dict[str, pd.Series | None] = { 'i': None, 't': None }
                object.__setattr__(res_ols, 'formula_str', formula_str)
                object.__setattr__(res_ols, 'structural_params', extract_structural(res_ols, mod))
                res = res_ols
            except Exception as e:
                with pd.ExcelWriter(dirs.tmp_dir / f"error_{model_name}.xlsx") as writer:
                    df_model.to_excel(writer, sheet_name='model_data', index=False)
                print(f"Wrote model data to {dirs.tmp_dir / f'error_{model_name}.xlsx'} for debugging.")
                raise e

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
                # Set property formula_str in res_gmm,
                # Knowing res_gmm is an immutable object, we can use object.__setattr__ to set the property
                object.__setattr__(res_gmm, 'formula_str', formula_str)
                object.__setattr__(res_gmm, 'structural_params', extract_structural(res_gmm, mod))
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
            object.__setattr__(res_ivpbox, 'structural_params', extract_structural(res_ivpbox, mod))
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

    # Modify res.summary. Split it by line and find the end of the parameters table (the line that starts with "===" after all the params).
    # If res.structural_params is not None, add the structural params in there
    summary_lines = str(res.summary).split('\n')
    i = 0
    for i, line in enumerate(summary_lines):
        if any([
            not line,
            line.startswith('F-test'),
            line.startswith('Endogenous:')
        ]):
            break
    if hasattr(res, 'structural_params') and res.structural_params is not None:     # type: ignore
        # Add parameter estimates to the table of the form:
        #             Parameter  Std. Err.     T-stat    P-value    Lower CI    Upper CI
        # year_2020      0.0116     0.0124     0.9376     0.3484     -0.0127      0.0359
        # year_2012      0.0101     0.0064     1.5856     0.1128     -0.0024      0.0225
        # wg1_y         -0.3843     0.1772    -2.1684     0.0301     -0.7317     -0.0369
        for k, v_tup in reversed(res.structural_params.items()):
            line = ""
            for v in v_tup:
                line += f"{v:>12.4f}"
            summary_lines.insert(i - 1, f"{k:<12}{line}")

    modified_summary = '\n'.join(summary_lines)

    output_str = ""
    output_str += f"Model '{model_name}': {mod.description}\n"
    if hasattr(res, 'formula_str') and res.formula_str is not None:      # type: ignore
        output_str += f"Formula: {res.formula_str}\n"       # type: ignore
    output_str += param_str + "\n"
    if hasattr(res, 'structural_params') and res.structural_params is not None:     # type: ignore
        output_str += "Structural Parameters: {" + ", ".join([f"{k}: {v[0]:.4f}" for k, v in res.structural_params.items()]) + "}\n"    # type: ignore
    output_str += f"{modified_summary}\n\n"
    output_str += "=" * 87 + "\n\n"
    if hasattr(res, 'j_stat') and res.j_stat is not None:       # type: ignore
        # Add to output_str in following pattern:
        # Hansen test of overid. restrictions: chi(5) = 4.990 Prob > Chi2 = 0.417
        output_str += f"Hansen test of overid. restrictions: chi({res.j_stat.df}) = {res.j_stat.stat:.3f} Prob > Chi2 = {res.j_stat.pval:.3f}\n"    # type: ignore  
        output_str += "Hansen J-statistic:\n"
        output_str += res.j_stat.__str__()                      # type: ignore
        output_str += '\n'

    return output_str