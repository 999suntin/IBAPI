from ib_insync import IB, Stock, Option, Order

# Connect to IBKR TWS (Trader Workstation) or IB Gateway
ib = IB()
ib.connect("127.0.0.1", 7497, clientId=1)  # Replace with your TWS/Gateway IP address and clientId

# Define contract details for Tesla and Apple stocks
tesla_stock_contract = Stock("TSLA", "SMART", "USD")
apple_stock_contract = Stock("AAPL", "SMART", "USD")

# Define contract details for Tesla and Apple call options (1 month expiration)
tesla_option_contract = Option("TSLA", "202112", 500, "C", "SMART", "USD")
apple_option_contract = Option("AAPL", "202112", 150, "C", "SMART", "USD")

# Request market data for Tesla and Apple stocks
tesla_stock_data = ib.reqMktData(tesla_stock_contract, genericTickList="233")
apple_stock_data = ib.reqMktData(apple_stock_contract, genericTickList="233")

# Request market data for Tesla and Apple call options
tesla_option_data = ib.reqMktData(tesla_option_contract, genericTickList="233")
apple_option_data = ib.reqMktData(apple_option_contract, genericTickList="233")

# Wait for market data to be available (you can adjust the timeout as needed)
ib.sleep(5)

# Place a long call order for Tesla (buy 1 call option)
tesla_order = Order(action="BUY", totalQuantity=1, orderType="LMT", lmtPrice=tesla_option_data.marketPrice())
tesla_trade = ib.placeOrder(tesla_option_contract, tesla_order)

# Place a long call order for Apple (buy 1 call option)
apple_order = Order(action="BUY", totalQuantity=1, orderType="LMT", lmtPrice=apple_option_data.marketPrice())
apple_trade = ib.placeOrder(apple_option_contract, apple_order)

# Print trade details for Tesla and Apple
print("Trade details for Tesla (TSLA) Call Option:")
print(tesla_trade)

print("\nTrade details for Apple (AAPL) Call Option:")
print(apple_trade)

# Disconnect from IBKR
ib.disconnect()
