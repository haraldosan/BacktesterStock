import pandas as pd
import numpy as np
import yfinance as yf
# from pandas_datareader import data as pdr
import datetime as dt


class Signals:

    def __init__(self, ticker):
        self.ticker = ticker

    def sma(self, hist, smatype, date):
        # hist = hist[(hist["Date"] <= date)][:-21:-1]
        hist = hist[(hist["Date"] <= date)][- smatype:]
        hist[f'SMA({smatype})'] = hist.Close.rolling(smatype).mean()
        # print(hist)
        return hist.loc[hist.index[-1], f'SMA({smatype})']

    # Calculates Exponential Moving Average for a specific date
    def ewa(self, hist, ewatype, date):
        pass

    def bollinger_bands(self, hist, bollingertype, date):
        hist = hist[(hist["Date"] <= date)][- bollingertype:]
        hist[f'Bollinger({bollingertype})'] = hist.Close.rolling(
            bollingertype).mean()

        hist[f'Bollinger Upper({bollingertype})'] = hist[f'Bollinger({bollingertype})'] + (
            hist.Close.rolling(bollingertype).std() * 2)
        hist[f'Bollinger Lower({bollingertype})'] = hist[f'Bollinger({bollingertype})'] - (
            hist.Close.rolling(bollingertype).std() * 2)

        return hist.loc[hist.index[-1], f'Bollinger Upper({bollingertype})'], hist.loc[hist.index[-1], f'Bollinger Lower({bollingertype})']

    def pct_change(self, hist):
        df = hist["Close"]
        percent = df.pct_change()
        return percent


if __name__ == "__main__":
    tsla = Signals("TSLA")
    hist = tsla.ticker.history(period="max")
    close = hist["Close"]

    # """
    # start_date = "2019-1-1"
    # end_date = "2019-1-31"

    # after_start_date = hist["date"] >= start_date
    # before_end_date = hist["date"] <= end_date
    # between_two_dates = after_start_date & before_end_date
    # filtered_dates = hist.loc[between_two_dates]
    # """
    # print(tsla.sma(hist, 20, "01-01-2019")
