def Volume_ratio(df, window=25):
    return (
        df["Volume"]
        / df["Volume"].rolling(window).mean()
        * 100
    )
