import yfinance as yf

from indicators.rename import rename_columns
from indicators.rsi import calc_rsi
from indicators.macd import calc_macd
from indicators.bollinger import calc_bollinger
from indicators.flpercent import flpercent
from indicators.hlpercent import hlpercent


def get_stock_data(symbol):
    ticker = yf.Ticker(symbol)

    df = ticker.history(period="1y")
    df = flpercent(df)
    df = hlpercent(df)

    df['MA5'] = df['Close'].rolling(5).mean()
    df['MA25'] = df['Close'].rolling(25).mean()
    df['MA75'] = df['Close'].rolling(75).mean()

    df['RSI7'] = calc_rsi(df, 7)
    df['RSI14'] = calc_rsi(df, 14)
    df['RSI28'] = calc_rsi(df, 28)
    df['MACD'], df['Signal'] = calc_macd(df)

    bb_ma, bb_std, upper1, lower1, upper2, lower2, upper3, lower3 = calc_bollinger(
        df, window=25, sigma=3)

    df['BB_MA25'] = bb_ma
    df['BB_STD25'] = bb_std

    df['BB_lower3'] = lower3
    df['BB_lower2'] = lower2
    df['BB_lower1'] = lower1
    df['BB_upper1'] = upper1
    df['BB_upper2'] = upper2
    df['BB_upper3'] = upper3

    return df
