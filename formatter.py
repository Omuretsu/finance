def prepare_ai_data(df, days=5):
    columns = [
        "Close",
        "Volume",
        "Volume_Ratio",
        "MA25",
        "MA75",
        "RSI7",
        "RSI14",
        "RSI28",
        "MACD",
        "Signal",
        "MACD_Gap",
        "HL_pct",
        "OC_pct",
        "BB_ZScore"
    ]

    return df[columns].tail(days)
