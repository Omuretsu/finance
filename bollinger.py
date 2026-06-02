def calc_bollinger(df, window=25, sigma=3):
    bb_ma = df['Close'].rolling(window).mean()
    bb_std = df['Close'].rolling(window).std()

    upper1 = bb_ma + (1 * bb_std)
    lower1 = bb_ma - (1 * bb_std)

    upper2 = bb_ma + (2 * bb_std)
    lower2 = bb_ma - (2 * bb_std)

    upper3 = bb_ma + (3 * bb_std)
    lower3 = bb_ma - (3 * bb_std)
    return bb_ma, bb_std, upper1, lower1, upper2, lower2, upper3, lower3
