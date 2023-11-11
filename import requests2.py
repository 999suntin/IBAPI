import requests
import pandas as pd

# Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual API key
ALPHA_VANTAGE_API_KEY = 'YOUR_ALPHA_VANTAGE_API_KEY'
ticker = 'TSLA'
option_symbol = 'TSLA210121C00550000'  # Example option symbol (TSLA, Exp: 2021-01-21, Call, Strike: $550)
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={option_symbol}&interval=1min&apikey={ALPHA_VANTAGE_API_KEY}'

# Fetch historical options data for the specified option symbol from Alpha Vantage API
response = requests.get(url)
data = response.json()['Time Series (1min)']
df = pd.DataFrame(data).T
df.index = pd.to_datetime(df.index)
df = df.sort_index()
df['Volume'] = df['5. volume'].astype(int)

# Calculate options volume spike threshold (you can adjust this threshold based on your analysis)
volume_spike_threshold = 2 * df['Volume'].mean()  # Example: 2 times the average volume

# Detect options volume spikes
df['VolumeSpike'] = df['Volume'] > volume_spike_threshold

# Create buy and sell signals based on volume spikes
df['Signal'] = 0
df['Signal'][df['VolumeSpike']] = 1  # Buy signal when there is a volume spike

# Print buy signals and corresponding timestamps
buy_signals = df[df['Signal'] == 1]
print("Buy Signals:")
print(buy_signals[['Volume', 'Signal']])

# Implement your trading logic based on the buy signals (this is a placeholder)
# Example: Execute a trade when there is a buy signal
# trade_executed = execute_trade()

# Note: In a real trading scenario, you should implement appropriate risk management and position sizing strategies.

# Visualize options volume and volume spikes (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
plt.plot(df.index, df['Volume'], label="Options Volume", linewidth=0.5)
plt.scatter(buy_signals.index, buy_signals['Volume'], color='g', marker='^', label='Buy Signals (Volume Spike)')
plt.title("Tesla Options Volume with Volume Spike Buy Signals")
plt.xlabel("Timestamp")
plt.ylabel("Volume")
plt.legend()
plt.show()
