from datetime import datetime


def generate_report(
    ticker,
    start_date,
    end_date,
    highest_price,
    lowest_price,
    volatility,
    insights
):

    report = f"""
==================================================
        STOCK MARKET ANALYSIS REPORT
==================================================

Generated On:
{datetime.now()}

--------------------------------------------------
STOCK INFORMATION
--------------------------------------------------

Ticker Symbol: {ticker}

Analysis Period:
{start_date} to {end_date}

--------------------------------------------------
PRICE ANALYSIS
--------------------------------------------------

Highest Price: {highest_price:.2f}

Lowest Price: {lowest_price:.2f}

Latest Close:
{insights['latest_close']:.2f}

Average Close:
{insights['average_close']:.2f}

--------------------------------------------------
RISK ANALYSIS
--------------------------------------------------

Volatility: {volatility:.4f}

Risk Level:
{insights['risk_level']}

--------------------------------------------------
TREND ANALYSIS
--------------------------------------------------

Trend:
{insights['trend']}

--------------------------------------------------
DISCLAIMER
--------------------------------------------------

Educational project only.

NOT financial advice.

==================================================
"""

    report_path = f"reports/{ticker}_financial_report.txt"

    with open(report_path, "w", encoding="utf-8") as file:
        file.write(report)

    print("\nReport generated successfully!")