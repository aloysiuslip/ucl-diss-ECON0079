import ibis
from ibis import _
import pandas as pd

from utils.f_0_dirs import get_data_dirs
dirs = get_data_dirs(segment="model")

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


def transform_nfe(values: list[str], fe: list[str], fe_type: str) -> list[str]:
    if 'lnfe' in fe:
        return [f"(i-w{fe_type}1){'_' if len(p) == 1 else ''}{p}" for p in values]
    elif 'gnfe' in fe:
        return [f"(i-v{fe_type}1){'_' if len(p) == 1 else ''}{p}" for p in values]
    else:
        return values