import pandas as pd
import numpy as nd
import yfinance as yf
from signals import Signals as sign


class Backtester:

    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)

    def get_sma(self):
        s = sign(self.ticker)
        return s.sma(20)


if __name__ == "__main__":
    tsla = Backtester("TSLA")
    hist = tsla.ticker.history(period="max")
    print(tsla.get_sma())
