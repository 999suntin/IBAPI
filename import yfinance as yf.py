import yfinance as yf
import pandas as pd

# Define the ticker symbols for Tesla and Apple
tesla_symbol = "TSLA"
apple_symbol = "AAPL"

# Set the start and end dates for the historical data (format: "YYYY-MM-DD")
start_date = "2022-01-01"
end_date = "2023-01-01"

# Get historical data for Tesla
tesla_data = yf.download(tesla_symbol, start=start_date, end=end_date)

# Get historical data for Apple
apple_data = yf.download(apple_symbol, start=start_date, end=end_date)

# Print the historical data for Tesla and Apple
print("Tesla Stock Data:")
print(tesla_data.head())  # Print the first 5 rows of Tesla data
print("\nApple Stock Data:")
print(apple_data.head())  # Print the first 5 rows of Apple data

# Optionally, you can save the data to a CSV file
tesla_data.to_csv("tesla_stock_data.csv")
apple_data.to_csv("apple_stock_data.csv")
