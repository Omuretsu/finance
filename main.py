from macd import calc_macd, signal
import yfinance as yf
from datetime import datetime
from pathlib import Path

from rename import rename_columns


from rsi import calc_rsi


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


def percent(df):
    df['OC_diff'] = df['Close'] - df['Open']
    df['OC_pct'] = (df['Close'] - df['Open']) / df['Open'] * 100
    return df


symbols = [
    "285A.T",
    "1542.T",
]


def get_stock_data(symbol):
    ticker = yf.Ticker(symbol)

    df = ticker.history(period="1y")

    df = percent(df)

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


save_dir = Path.home() / "Desktop" / "31_finance"
save_dir.mkdir(parents=True, exist_ok=True)

for symbol in symbols:
    df = get_stock_data(symbol)
    df = rename_columns(df)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_symbol = symbol.split(".")[0]

    filepath = save_dir / f"{file_symbol}_{timestamp}.csv"

    df.to_csv(filepath)
    print(f"保存完了: {filepath}")
