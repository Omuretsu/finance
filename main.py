from datetime import datetime
from pathlib import Path
from data_loader import get_stock_data
from indicators.rename import rename_columns

symbols = [
    "285A.T",
    "1542.T",
]

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
