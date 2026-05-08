from src.data_fetcher import fetch_stock_data

from src.analyzer import (
    clean_data,
    calculate_daily_returns,
    calculate_moving_averages,
    calculate_volatility,
    get_price_statistics,
    generate_insights
)

from src.visualizer import (
    plot_closing_price,
    plot_moving_averages,
    plot_return_distribution
)

from src.report_generator import generate_report


# ==========================================
# USER INPUT
# ==========================================

TICKER = "AAPL"

START_DATE = "2023-01-01"

END_DATE = "2024-01-01"


# ==========================================
# FETCH DATA
# ==========================================

stock_df = fetch_stock_data(
    TICKER,
    START_DATE,
    END_DATE
)


# ==========================================
# CLEAN DATA
# ==========================================

stock_df = clean_data(stock_df)


# ==========================================
# RETURNS
# ==========================================

stock_df = calculate_daily_returns(stock_df)


# ==========================================
# MOVING AVERAGES
# ==========================================

stock_df = calculate_moving_averages(stock_df)


# ==========================================
# VOLATILITY
# ==========================================

volatility = calculate_volatility(stock_df)


# ==========================================
# PRICE STATS
# ==========================================

highest_price, lowest_price = get_price_statistics(stock_df)


# ==========================================
# INSIGHTS
# ==========================================

insights = generate_insights(stock_df, volatility)


# ==========================================
# PRINT SUMMARY
# ==========================================

print("\n==============================")

print(" STOCK MARKET ANALYSIS ")

print("==============================")

print(f"Ticker: {TICKER}")

print(f"Highest Price: {highest_price:.2f}")

print(f"Lowest Price: {lowest_price:.2f}")

print(f"Volatility: {volatility:.4f}")

print(f"Trend: {insights['trend']}")

print(f"Risk Level: {insights['risk_level']}")


# ==========================================
# VISUALIZATION
# ==========================================

plot_closing_price(stock_df, TICKER)

plot_moving_averages(stock_df, TICKER)

plot_return_distribution(stock_df, TICKER)


# ==========================================
# REPORT
# ==========================================

generate_report(
    TICKER,
    START_DATE,
    END_DATE,
    highest_price,
    lowest_price,
    volatility,
    insights
)

print("\nCharts saved in images folder.")

print("Reports saved in reports folder.")

print("Project executed successfully!")