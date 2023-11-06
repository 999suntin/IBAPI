import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Fetch historical data for Tesla (TSLA) stock from Yahoo Finance
ticker = "TSLA"
data = yf.download(ticker, start="2015-01-01", end="2023-01-01")

# Calculate 50-day and 200-day moving averages
data["MA50"] = data["Close"].rolling(window=50).mean()
data["MA200"] = data["Close"].rolling(window=200).mean()

# Create signals based on moving average crossovers
data["Signal"] = 0  # 0 means no signal, 1 means buy, -1 means sell
data["Signal"][50:] = 0  # Start signals from the 50th row to match the moving average window
data["Signal"][50:] = data["MA50"][50:] > data["MA200"][50:]
data["Signal"] = data["Signal"].astype(int)
data["Position"] = data["Signal"].diff()

# Backtest the strategy and calculate returns
initial_balance = 100000  # Initial balance in USD
balance = initial_balance
for index, row in data.iterrows():
    if row["Position"] == 1:  # Buy signal
        balance -= row["Close"]  # Deduct the buy price from the balance
    elif row["Position"] == -1:  # Sell signal
        balance += row["Close"]  # Add the sell price to the balance

# Calculate final balance
final_balance = balance + data["Close"].iloc[-1] * data["Position"].iloc[-1]

# Print the backtest results
print("Initial Balance: $", initial_balance)
print("Final Balance: $", final_balance)
print("Profit/Loss: $", final_balance - initial_balance)

# Visualize the data and strategy
plt.figure(figsize=(14, 7))
plt.plot(data.index, data["Close"], label="Tesla Close Price", linewidth=0.5)
plt.plot(data.index, data["MA50"], label="50-day Moving Average", linewidth=1)
plt.plot(data.index, data["MA200"], label="200-day Moving Average", linewidth=1)
plt.plot(data[data["Signal"] == 1].index, data["MA50"][data["Signal"] == 1], '^', markersize=10, color='g', label='Buy Signal')
plt.plot(data[data["Signal"] == -1].index, data["MA50"][data["Signal"] == -1], 'v', markersize=10, color='r', label='Sell Signal')
plt.title("Tesla Stock Price with Moving Average Crossover Strategy")
plt.xlabel("Year")
plt.ylabel("Price")
plt.legend()
plt.show()
