import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="Stock Market Data Analyzer",
    page_icon="📈",
    layout="wide"
)


# =========================================
# TITLE
# =========================================

st.title("📈 Stock Market Data Analyzer")

st.markdown("### Industry-Level Financial Analytics Dashboard")


# =========================================
# SIDEBAR
# =========================================

st.sidebar.header("User Input")


ticker = st.sidebar.text_input(
    "Enter Stock Ticker",
    "AAPL"
)


start_date = st.sidebar.date_input(
    "Start Date"
)


end_date = st.sidebar.date_input(
    "End Date"
)


# =========================================
# BUTTON
# =========================================

if st.sidebar.button("Analyze Stock"):

    with st.spinner("Fetching stock data..."):

        df = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            auto_adjust=False
        )

        # Fix MultiIndex columns
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)


    # =========================================
    # CHECK DATA
    # =========================================

    if df.empty:

        st.error("No stock data found.")

    else:

        # =========================================
        # CALCULATIONS
        # =========================================

        df['Daily Return'] = df['Close'].pct_change()

        df['MA20'] = df['Close'].rolling(window=20).mean()

        df['MA50'] = df['Close'].rolling(window=50).mean()

        volatility = df['Daily Return'].std()

        highest_price = float(df['High'].max())

        lowest_price = float(df['Low'].min())

        latest_close = float(df['Close'].iloc[-1])

        average_close = float(df['Close'].mean())


        # =========================================
        # METRICS
        # =========================================

        st.subheader("📊 Stock Summary")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Latest Close",
            f"${latest_close:.2f}"
        )

        col2.metric(
            "Highest Price",
            f"${highest_price:.2f}"
        )

        col3.metric(
            "Lowest Price",
            f"${lowest_price:.2f}"
        )

        col4.metric(
            "Volatility",
            f"{volatility:.4f}"
        )


        # =========================================
        # DATASET
        # =========================================

        st.subheader("📁 Full Dataset")

        st.dataframe(df, use_container_width=True)


        # =========================================
        # CLOSING PRICE CHART
        # =========================================

        st.subheader("📈 Closing Price Analysis")

        fig_close = px.line(
            df,
            x=df.index,
            y='Close',
            title=f'{ticker} Closing Price'
        )

        st.plotly_chart(
            fig_close,
            use_container_width=True
        )


        # =========================================
        # MOVING AVERAGES
        # =========================================

        st.subheader("📉 Moving Average Analysis")

        fig_ma = go.Figure()

        fig_ma.add_trace(
            go.Scatter(
                x=df.index,
                y=df['Close'],
                mode='lines',
                name='Close Price'
            )
        )

        fig_ma.add_trace(
            go.Scatter(
                x=df.index,
                y=df['MA20'],
                mode='lines',
                name='20-Day MA'
            )
        )

        fig_ma.add_trace(
            go.Scatter(
                x=df.index,
                y=df['MA50'],
                mode='lines',
                name='50-Day MA'
            )
        )

        fig_ma.update_layout(
            title="Moving Average Analysis"
        )

        st.plotly_chart(
            fig_ma,
            use_container_width=True
        )


        # =========================================
        # DAILY RETURN ANALYSIS
        # =========================================

        st.subheader("📊 Daily Return Analysis")

        fig_return = px.line(
            df,
            x=df.index,
            y='Daily Return',
            title='Daily Returns'
        )

        st.plotly_chart(
            fig_return,
            use_container_width=True
        )


        # =========================================
        # RETURN DISTRIBUTION
        # =========================================

        st.subheader("📌 Return Distribution")

        fig_dist, ax = plt.subplots(figsize=(12, 5))

        sns.histplot(
            df['Daily Return'].dropna(),
            bins=50,
            ax=ax
        )

        st.pyplot(fig_dist)


        # =========================================
        # STATISTICS
        # =========================================

        st.subheader("📋 Statistical Summary")

        st.write(df.describe())


        # =========================================
        # DOWNLOAD CSV
        # =========================================

        st.subheader("⬇ Download Dataset")

        csv = df.to_csv().encode('utf-8')

        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f'{ticker}_stock_data.csv',
            mime='text/csv'
        )


        # =========================================
        # FINANCIAL INSIGHTS
        # =========================================

        st.subheader("🧠 Financial Insights")

        trend = "Bullish"

        if latest_close < average_close:
            trend = "Bearish"

        st.success(f"Market Trend: {trend}")


        if volatility > 0.02:

            st.warning(
                "High volatility detected. Higher investment risk."
            )

        else:

            st.info(
                "Moderate market volatility detected."
            )


        # =========================================
        # DISCLAIMER
        # =========================================

        st.warning(
    "DISCLAIMER: This dashboard is built for educational and portfolio purposes only. It does NOT provide financial or investment advice."
)

        st.success(
            "Analysis Completed Successfully!"
        )