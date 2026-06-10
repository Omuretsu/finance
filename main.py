from data_loader import get_stock_data
from indicators.rename import rename_columns
from utils.file_io import setup_save_dir
from utils.time_utils import get_timestamp
from formatter import prepare_ai_data

from symbols import SYMBOLS, period, days

try:
    import config_local
except ImportError:
    config_local = None

if config_local:
    SYMBOLS = getattr(config_local, "SYMBOLS", SYMBOLS)
    period = getattr(config_local, "period", period)
    days = getattr(config_local, "days", days)

save_dir = setup_save_dir()

for symbol in SYMBOLS:
    df = get_stock_data(symbol, period=period)
    print(symbol, "raw df shape:", df.shape)
    ai_df = prepare_ai_data(df, days=days)
    ai_df.index = ai_df.index.strftime("%Y-%m-%d")
    ai_df = rename_columns(ai_df)

    timestamp = get_timestamp()
    filepath = save_dir / f"{symbol}_{timestamp}.csv"
    ai_df.to_csv(filepath)
    print(f"保存完了: {filepath}")
