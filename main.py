import yfinance as yf
from datetime import datetime
from pathlib import Path

symbol = "285A.T"
ticker = yf.Ticker(symbol)

df = ticker.history(period="120d")

df["MA5"] = df["Close"].rolling(5).mean()
df["MA25"] = df["Close"].rolling(25).mean()
df["MA75"] = df["Close"].rolling(75).mean()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_symbol = symbol.split(".")[0]
filename = f"{file_symbol}_{timestamp}.csv"

save_dir = Path.home() / "Desktop" / "31_finance"
save_dir.mkdir(parents=True, exist_ok=True)

filepath = save_dir / f"{file_symbol}_{timestamp}.csv"

df.to_csv(filepath)
print(f"保存完了: {filepath}")
