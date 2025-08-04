import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
start_date = '2020-01-01'
end_date = '2023-01-01'

adj_close = pd.DataFrame()

# Download each stock with auto_adjust=False so 'Adj Close' appears
for ticker in tickers:
    stock_data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False)
    adj_close[ticker] = stock_data['Adj Close']  # This line now works

# Drop rows with any missing values
adj_close.dropna(inplace=True)

# Plot stock prices
plt.figure(figsize=(14, 6))
for ticker in tickers:
    plt.plot(adj_close.index, adj_close[ticker], label=ticker)
plt.title("Stock Price Over Time")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Amazon-specific analysis
amazon = yf.download('AMZN', start=start_date, end=end_date, auto_adjust=False)

plt.figure(figsize=(12, 5))
amazon['Volume'].plot(title='Amazon Volume Traded')
plt.xlabel("Date")
plt.ylabel("Volume")
plt.grid()
plt.tight_layout()
plt.show()

amazon['MA20'] = amazon['Adj Close'].rolling(20).mean()
amazon['MA50'] = amazon['Adj Close'].rolling(50).mean()

amazon[['Adj Close', 'MA20', 'MA50']].plot(figsize=(14, 6), title='Amazon Moving Averages')
plt.tight_layout()
plt.grid()
plt.show()

amazon['Daily Return'] = amazon['Adj Close'].pct_change()
amazon['Trend'] = amazon['Daily Return'].apply(lambda x: 'Positive' if x > 0 else 'Negative' if x < 0 else 'No Change')

trend_counts = amazon['Trend'].value_counts()
trend_counts.plot.pie(autopct='%1.1f%%', startangle=90, figsize=(6, 6), title='Amazon Daily Trend')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Correlation between stocks
daily_returns = adj_close.pct_change()
plt.figure(figsize=(10, 6))
sns.heatmap(daily_returns.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Between Stocks (Daily Returns)")
plt.tight_layout()
plt.show()
