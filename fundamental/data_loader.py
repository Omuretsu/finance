import os
import requests
import pandas as pd

from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.jquants.com"


def get_financial_summary(code: str) -> pd.DataFrame:
    """
    J-Quants 財務サマリー取得

    Parameters
    ----------
    code : str
        証券コード(例: 7203)

    Returns
    -------
    pd.DataFrame
    """

    api_key = os.getenv("JQUANTS_API_KEY")

    if not api_key:
        raise ValueError(
            "環境変数 JQUANTS_API_KEY が設定されていません"
        )

    headers = {
        "x-api-key": api_key,
    }

    params = {
        "code": code,
    }

    response = requests.get(
        f"{BASE_URL}/v2/fins/summary",
        headers=headers,
        params=params,
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    # 実データ部分
    records = data.get("data", [])

    return pd.DataFrame(records)
