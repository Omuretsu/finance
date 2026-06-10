from symbols import SYMBOLS
from fundamental.data_loader import get_financial_summary
from fundamental.formatter import (
    select_columns,
    convert_numeric,
)
from fundamental.analyzer import analyze_fundamentals
from utils.file_io import setup_save_dir, save_csv
from utils.time_utils import get_timestamp
from utils.symbol_utils import to_jquants_code


def main(code: str):
    df = get_financial_summary(code)

    save_dir = setup_save_dir()

    df = select_columns(df)
    df = convert_numeric(df)

    result = analyze_fundamentals(df)
    timestamp = get_timestamp()

    filepath = save_dir / f"{code}_fundamental_{timestamp}.csv"
    save_csv(result, filepath)

    print(
        result[
            [
                "DiscDate",
                "SalesGrowth",
                "EPSGrowth",
                "ForecastEPSGrowth",
                "OperatingMargin",
                "ROE",
                "EquityRatio",
                "DividendPayoutRatio",
            ]
        ]
    )


if __name__ == "__main__":
    for code in SYMBOLS:
        jcode = to_jquants_code(code)
        main(jcode)
