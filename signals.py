import pandas as pd
import numpy as np
import yfinance as yf
from pandas_datareader import data as pdr
import datetime as dt


class Signals:

    def __init__(self, ticker):
        self.ticker = ticker

    def sma(self, smatype):
        try:
            hist = self.ticker.history(period="max")
            hist[f'SMA({smatype})'] = hist.Close.rolling(smatype).mean()
            return hist[f'SMA({smatype})'][-1]
        except:
            return None


if __name__ == "__main__":
    tsla = Signals("TSLA")
    hist = tsla.ticker.history(period="max")
    close = hist["Close"]

    start_date = "2019-1-1"
    end_date = "2019-1-31"

    after_start_date = hist["date"] >= start_date
    before_end_date = hist["date"] <= end_date
    between_two_dates = after_start_date & before_end_date
    filtered_dates = hist.loc[between_two_dates]

    print(close)
