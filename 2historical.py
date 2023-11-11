import yfinance as yf
import pandas as pd

# List of top 10 DJIA components based on market capitalization
top_djia_components = ["AAPL", "MSFT", "V", "JNJ", "PG", "JPM", "WMT", "KO", "MCD", "HD"]

# Set the start and end dates for the historical data (format: 'YYYY-MM-DD')
start_date = "2020-01-01"
end_date = "2023-01-01"

# Dictionary to store historical data for each component
historical_data = {}

# Download historical data for each component and store it in the dictionary
for ticker in top_djia_components:
    data = yf.download(ticker, start=start_date, end=end_date)
    historical_data[ticker] = data

# Save the historical data for each component to separate CSV files
for ticker, data in historical_data.items():
    data.to_csv(f"{ticker}_historical_data.csv")
    print(f"Data for {ticker} saved to {ticker}_historical_data.csv")
