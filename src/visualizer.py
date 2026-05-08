import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style("darkgrid")


def plot_closing_price(df, ticker):

    plt.figure(figsize=(14, 6))

    plt.plot(df.index, df['Close'])

    plt.title(f'{ticker} Closing Price')

    plt.xlabel('Date')

    plt.ylabel('Price')

    plt.tight_layout()

    path = f'images/{ticker}_closing_price.png'

    plt.savefig(path)

    plt.close()


def plot_moving_averages(df, ticker):

    plt.figure(figsize=(14, 6))

    plt.plot(df.index, df['Close'], label='Close Price')

    plt.plot(df.index, df['MA20'], label='20-Day MA')

    plt.plot(df.index, df['MA50'], label='50-Day MA')

    plt.title(f'{ticker} Moving Average Analysis')

    plt.xlabel('Date')

    plt.ylabel('Price')

    plt.legend()

    plt.tight_layout()

    path = f'images/{ticker}_moving_average.png'

    plt.savefig(path)

    plt.close()


def plot_return_distribution(df, ticker):

    plt.figure(figsize=(12, 6))

    sns.histplot(df['Daily Return'].dropna(), bins=50)

    plt.title(f'{ticker} Return Distribution')

    plt.tight_layout()

    path = f'images/{ticker}_return_distribution.png'

    plt.savefig(path)

    plt.close()