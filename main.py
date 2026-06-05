from data_loader import get_stock_data
from indicators.rename import rename_columns
from utils.file_io import setup_save_dir
from utils.time_utils import get_timestamp
from formatter import prepare_ai_data

symbols = [
    "1542.T",
]

save_dir = setup_save_dir()

for symbol in symbols:
    df = get_stock_data(symbol)
    ai_df = prepare_ai_data(df)
    ai_df = rename_columns(ai_df)

    timestamp = get_timestamp()
    filepath = save_dir / f"{symbol}_{timestamp}.csv"
    ai_df.to_csv(filepath)
    print(f"保存完了: {filepath}")
