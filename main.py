from data_loader import get_stock_data
from indicators.rename import rename_columns
from utils.file_io import setup_save_dir
from utils.time_utils import get_timestamp

symbols = [
    "285A.T",
    "1542.T",
]

save_dir = setup_save_dir()

for symbol in symbols:

    df = get_stock_data(symbol)
    df = rename_columns(df)
    timestamp = get_timestamp()
    filepath = save_dir / f"{symbol}_{timestamp}.csv"

    df.to_csv(filepath)
    print(f"保存完了: {filepath}")
