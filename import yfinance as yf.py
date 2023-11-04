import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the ticker symbols for Tesla and Apple
tesla_ticker = "TSLA"
apple_ticker = "APPL"

# Fetch historical data for Tesla
tesla_data = yf.Ticker(tesla_ticker)
tesla_history = tesla_data.history(period="max")

# Fetch historical data for Apple
apple_data = yf.Ticker(apple_ticker)
apple_history = apple_data.history(period="max")

# Calculate correlation matrix
correlation_matrix = pd.concat([tesla_history['Close'], apple_history['Close']], axis=1).corr()

# Create a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap between Tesla and Apple Stock Prices')
plt.show()
