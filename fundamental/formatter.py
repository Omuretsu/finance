import pandas as pd

USE_COLUMNS = [
    "DiscDate",
    "CurPerType",
    "Sales",
    "OP",
    "NP",
    "EPS",
    "TA",
    "Eq",
    "EqAR",
    "CFO",
    "DivAnn",
    "PayoutRatioAnn",
    "NxFSales",
    "NxFOP",
    "NxFNp",
    "NxFEPS",
]


NUMERIC_COLUMNS = [
    "Sales",
    "OP",
    "NP",
    "EPS",
    "TA",
    "Eq",
    "EqAR",
    "CFO",
    "DivAnn",
    "PayoutRatioAnn",
    "NxFSales",
    "NxFOP",
    "NxFNp",
    "NxFEPS",
]


def select_columns(df: pd.DataFrame) -> pd.DataFrame:
    return df[USE_COLUMNS].copy()


def convert_numeric(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce",
        )

    return df
