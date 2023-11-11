from ib_insync import *
util.startLoop()  # Enable asyncio event loop

# Connect to IBKR TWS (Trader Workstation) or IB Gateway
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)  # Replace with your TWS/Gateway IP address and clientId

# Define trading parameters
symbol_aapl = 'AAPL'
symbol_tsla = 'TSLA'
quantity = 100  # Number of shares to trade
order_type = 'MKT'  # Market order type (you can change this to limit order or other types)
exchange = 'SMART'  # Exchange to trade on (SMART routes the order to the best available exchange)

# Place trades for Apple (AAPL) and Tesla (TSLA) stocks
aapl_contract = Stock(symbol=symbol_aapl, exchange=exchange, currency='USD')
tsla_contract = Stock(symbol=symbol_tsla, exchange=exchange, currency='USD')

# Place market order to buy AAPL shares
aapl_order = MarketOrder('BUY', quantity)
trade_aapl = ib.placeOrder(aapl_contract, aapl_order)

# Place market order to buy TSLA shares
tsla_order = MarketOrder('BUY', quantity)
trade_tsla = ib.placeOrder(tsla_contract, tsla_order)

# Wait for the orders to be filled (you can implement more sophisticated logic for order status checking)
ib.sleep(2)  # Wait for 2 seconds

# Print trade details
print("AAPL Trade Details:")
print(trade_aapl)
print("TSLA Trade Details:")
print(trade_tsla)

# Disconnect from IBKR
ib.disconnect()
