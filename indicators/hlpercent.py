def hlpercent(df):
    df["HL_diff"] = df["High"] - df["Low"]
    df["HL_pct"] = (df["High"] - df["Low"]) / df["Open"] * 100

    df["body_pct"] = (
        (df["Close"] - df["Open"]) /
        (df["High"] - df["Low"])) * 100
    return df
