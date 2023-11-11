from ibapi.order import *
import ta
import numpy as np
import pandas as pd
import pytz
import math
from datetime import datetime, timedelta
import threading
import time
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

# Vars
orderId = 1


class IBApi(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)
        self.bars = []
        self.currentBar = None

    def historicalData(self, reqId, bar):
        self.bars.append(bar)

    def historicalDataEnd(self, reqId, start, end):
        bot.on_bar_update(self.bars, True)
        self.bars = []

    def realtimeBar(self, reqId, time, open_, high, low, close, volume, wap, count):
        bar = Bar()
        bar.open = open_
        bar.high = high
        bar.low = low
        bar.close = close
        bar.volume = volume
        bar.date = datetime.utcfromtimestamp(time).strftime('%Y%m%d %H:%M:%S')
        bot.on_bar_update([bar], False)


class Bar:
    def __init__(self):
        self.open = 0
        self.low = 0
        self.high = 0
        self.close = 0
        self.volume = 0
        self.date = ''


class Bot:
    ib = None
    barsize = 1
    currentBar = Bar()
    ema1Period = 9
    ema2Period = 21
    symbol = ""

    def __init__(self):
        self.ib = IBApi()
        self.ib.connect("127.0.0.1", 7496, 1)
        self.ib_thread = threading.Thread(target=self.ib.run, daemon=True)
        self.ib_thread.start()
        time.sleep(1)
        self.symbol = input("Enter the symbol/ticker you want to trade: ")
        self.barsize = int(input("Enter the barsize you want to trade in minutes: "))

        contract = Contract()
        contract.symbol = self.symbol
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"
        self.ib.reqHistoricalData(1, contract, "", "2 D", str(self.barsize) + " min", "MIDPOINT", 0, 1, False, [])

    def on_bar_update(self, bars, realtime):
        if realtime:
            bar = bars[0]
            self.currentBar = bar
            self.bars.append(bar)
        else:
            self.bars += bars

        if len(self.bars) >= max(self.ema1Period, self.ema2Period):
            closes = [bar.close for bar in self.bars]
            self.calculate_ema_signals(closes)

    def calculate_ema_signals(self, closes):
        ema1 = ta.trend.ema_indicator(np.array(closes), window=self.ema1Period)
        ema2 = ta.trend.ema_indicator(np.array(closes), window=self.ema2Period)
        if ema1[-1] > ema2[-1] and ema1[-2] <= ema2[-2]:
            print("BUY SIGNAL")
            # Implement your buy order logic here using self.ib.placeOrder(...)
        elif ema1[-1] < ema2[-1] and ema1[-2] >= ema2[-2]:
            print("SELL SIGNAL")
            # Implement your sell order logic here using self.ib.placeOrder(...)


# Start bot
bot = Bot()
