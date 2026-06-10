import pandas as pd


def get_fy_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    本決算(FY)のみ抽出
    """
    return df[df["CurPerType"] == "FY"].copy()


def add_profit_margin(df: pd.DataFrame) -> pd.DataFrame:
    """
    営業利益率(%)
    """
    df = df.copy()

    df["OperatingMargin"] = (
        df["OP"] / df["Sales"] * 100
    )

    return df


def add_growth_rates(df: pd.DataFrame) -> pd.DataFrame:
    """
    売上高成長率(%)
    EPS成長率(%)
    """
    df = df.copy()

    df["SalesGrowth"] = (
        df["Sales"].pct_change() * 100
    )

    df["EPSGrowth"] = (
        df["EPS"].pct_change() * 100
    )

    return df


def add_roe(df: pd.DataFrame) -> pd.DataFrame:
    """
    ROE(%)
    """
    df = df.copy()

    df["ROE"] = (
        df["NP"] / df["Eq"] * 100
    )

    return df


def add_forecast_growth(df: pd.DataFrame) -> pd.DataFrame:
    """
    来期予想EPS成長率(%)
    """
    df = df.copy()

    df["ForecastEPSGrowth"] = (
        (df["NxFEPS"] - df["EPS"])
        / df["EPS"]
        * 100
    )

    return df


def add_dividend_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    配当関連
    """
    df = df.copy()

    df["DividendPayoutRatio"] = (
        df["PayoutRatioAnn"] * 100
    )

    return df


def add_equity_ratio(df: pd.DataFrame) -> pd.DataFrame:
    """
    自己資本比率(%)
    """
    df = df.copy()

    df["EquityRatio"] = (
        df["EqAR"] * 100
    )

    return df


def analyze_fundamentals(df: pd.DataFrame) -> pd.DataFrame:

    df = df.sort_values("DiscDate").copy()

    # FYフラグ
    df["is_fy"] = df["CurPerType"] == "FY"

    # FYだけで成長率計算（疎構造維持）
    df["SalesGrowth"] = df["Sales"].where(df["is_fy"]).pct_change() * 100
    df["EPSGrowth"] = df["EPS"].where(df["is_fy"]).pct_change() * 100

    # 他指標はFYでも四半期でもOK
    df["OperatingMargin"] = df["OP"] / df["Sales"] * 100
    df["ROE"] = df["NP"] / df["Eq"] * 100
    df["EquityRatio"] = df["EqAR"] * 100
    df["DividendPayoutRatio"] = df["PayoutRatioAnn"] * 100

    df["ForecastEPSGrowth"] = (
        (df["NxFEPS"] - df["EPS"]) / df["EPS"] * 100
    )

    # 表示用に丸める（最終処理）
    num_cols = df.select_dtypes(include=["float", "int"]).columns
    df[num_cols] = df[num_cols].round(2)

    return df
