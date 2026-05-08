import pandas as pd
import numpy as np


def clean_data(df):

    print("\nCleaning stock data...")

    df = df.copy()

    df.dropna(inplace=True)

    return df


def calculate_daily_returns(df):

    df['Daily Return'] = df['Close'].pct_change()

    return df


def calculate_moving_averages(df):

    df['MA20'] = df['Close'].rolling(window=20).mean()

    df['MA50'] = df['Close'].rolling(window=50).mean()

    return df


def calculate_volatility(df):

    volatility = df['Daily Return'].std()

    return volatility


def get_price_statistics(df):

    highest_price = float(df['High'].max())

    lowest_price = float(df['Low'].min())

    return highest_price, lowest_price


def generate_insights(df, volatility):

    latest_close = float(df['Close'].iloc[-1])

    average_close = float(df['Close'].mean())

    trend = "Bullish"

    if latest_close < average_close:
        trend = "Bearish"

    risk_level = "Low"

    if volatility > 0.02:
        risk_level = "High"

    elif volatility > 0.01:
        risk_level = "Medium"

    insights = {
        "trend": trend,
        "risk_level": risk_level,
        "latest_close": latest_close,
        "average_close": average_close
    }

    return insights