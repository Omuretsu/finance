from fundamental.data_loader import get_financial_summary
from fundamental.formatter import (
    select_columns,
    convert_numeric,
)
from fundamental.analyzer import (
    analyze_fundamentals,
)


def main():
    df = get_financial_summary("7203")

    df = select_columns(df)
    df = convert_numeric(df)

    result = analyze_fundamentals(df)

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
    main()
