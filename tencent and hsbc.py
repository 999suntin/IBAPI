import yfinance as yf
import pandas as pd

# Define the ticker symbol for Tencent (0700.HK)
tencent_symbol = "0700.HK"

# Set the start and end dates for the historical data (format: "YYYY-MM-DD")
start_date = "2022-01-01"
end_date = "2023-01-01"

# Get historical data for Tencent
tencent_data = yf.download(tencent_symbol, start=start_date, end=end_date)

# Save the Tencent data to a CSV file
tencent_data.to_csv("tencent_stock_data.csv")

# Print a message indicating that the data has been saved
print("Tencent stock data has been saved to CSV file.")
