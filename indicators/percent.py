def percent(df):
    df['OC_diff'] = df['Close'] - df['Open']
    df['OC_pct'] = (df['Close'] - df['Open']) / df['Open'] * 100
    return df
