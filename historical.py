import yfinance as yf
import pandas as pd

# Define the ticker symbols for Tencent and HSBC
tencent_ticker = "0700.HK"  # Tencent Holdings Limited on the Hong Kong Stock Exchange
hsbc_ticker = "0005.HK"      # HSBC Holdings plc on the Hong Kong Stock Exchange

# Set the start and end dates for the historical data (format: 'YYYY-MM-DD')
start_date = "2020-01-01"
end_date = "2023-01-01"

# Download historical data for Tencent
tencent_data = yf.download(tencent_ticker, start=start_date, end=end_date)

# Download historical data for HSBC
hsbc_data = yf.download(hsbc_ticker, start=start_date, end=end_date)

# Save the dataframes to CSV files
tencent_data.to_csv("tencent_stock_data.csv")
hsbc_data.to_csv("hsbc_stock_data.csv")

# Print a message indicating that the data has been saved
print("Data saved to CSV files: tencent_stock_data.csv and hsbc_stock_data.csv")
