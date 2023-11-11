import requests
import pandas as pd
import matplotlib.pyplot as plt

# Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual API key
ALPHA_VANTAGE_API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
ticker = 'TSLA'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_VANTAGE_API_KEY}'

# Fetch historical data for Tesla (TSLA) stock from Alpha Vantage API
response = requests.get(url)
data = response.json()['Time Series (Daily)']
df = pd.DataFrame(data).T
df.index = pd.to_datetime(df.index)
df = df.sort_index()
df['Close'] = df['4. close'].astype(float)

# Calculate 50-day and 200-day moving averages
df["MA50"] = df["Close"].rolling(window=50).mean()
df["MA200"] = df["Close"].rolling(window=200).mean()

# Create signals based on moving average crossovers
df["Signal"] = 0  # 0 means no signal, 1 means buy, -1 means sell
df["Signal"][50:] = df["MA50"][50:] > df["MA200"][50:]
df["Signal"] = df["Signal"].astype(int)
df["Position"] = df["Signal"].diff()

# Backtest the strategy and calculate returns
initial_balance = 100000  # Initial balance in USD
balance = initial_balance
for index, row in df.iterrows():
    if row["Position"] == 1:  # Buy signal
        balance -= row["Close"]  # Deduct the buy price from the balance
    elif row["Position"] == -1:  # Sell signal
        balance += row["Close"]  # Add the sell price to the balance

# Calculate final balance
final_balance = balance + df["Close"].iloc[-1] * df["Position"].iloc[-1]

# Print the backtest results
print("Initial Balance: $", initial_balance)
print("Final Balance: $", final_balance)
print("Profit/Loss: $", final_balance - initial_balance)

# Visualize the data and strategy
plt.figure(figsize=(14, 7))
plt.plot(df.index, df["Close"], label="Tesla Close Price", linewidth=0.5)
plt.plot(df.index, df["MA50"], label="50-day Moving Average", linewidth=1)
plt.plot(df.index, df["MA200"], label="200-day Moving Average", linewidth=1)
plt.plot(df[df["Signal"] == 1].index, df["MA50"][df["Signal"] == 1], '^', markersize=10, color='g', label='Buy Signal')
plt.plot(df[df["Signal"] == -1].index, df["MA50"][df["Signal"] == -1], 'v', markersize=10, color='r', label='Sell Signal')
plt.title("Tesla Stock Price with Moving Average Crossover Strategy")
plt.xlabel("Year")
plt.ylabel("Price")
plt.legend()
plt.show()
