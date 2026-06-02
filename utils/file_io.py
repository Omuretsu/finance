from pathlib import Path
from datetime import datetime


def setup_save_dir():
    save_dir = Path.home() / "Desktop" / "31_finance"
    save_dir.mkdir(parents=True, exist_ok=True)
    return save_dir
