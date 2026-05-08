import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch stock data from Yahoo Finance
    """

    print(f"\nFetching stock data for {ticker}...")

    df = yf.download(
        ticker,
        start=start_date,
        end=end_date,
        auto_adjust=False
    )

    if df.empty:
        raise ValueError("No stock data found.")

    # Fix multi-column issue
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    csv_path = f"data/raw/{ticker}_stock_data.csv"

    df.to_csv(csv_path)

    print("Stock data fetched successfully!")
    print(df.head())

    return df