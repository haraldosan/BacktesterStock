import pandas as pd
import numpy as nd
import yfinance as yf
from signals import Signals as sign


class Backtester:

    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)
        self.hist = self.ticker.history(period="max")
        self.hist.reset_index(inplace=True)

    def get_sma_for_date(self, date, smatype):
        s = sign(self.ticker)
        return s.sma(self.hist, smatype, date)

    def get_sma_time_period(self, window):
        dates_and_sma = []
        for date in self.hist["Date"][- window:]:
            dates_and_sma.append((date, self.get_sma_for_date(date, window)))

        return dates_and_sma

    def get_bollinger_bands_for_date(self, date, bollingertype):
        s = sign(self.ticker)
        return s.bollinger_bands(self.hist, bollingertype, date)

    def get_bollinger_band_time_period(self, window):
        dates_and_bollinger_bands = []
        for date in self.hist["Date"][- window:]:
            dates_and_bollinger_bands.append(
                (date, self.get_bollinger_bands_for_date(date, window)))

        return dates_and_bollinger_bands


if __name__ == "__main__":
    tsla = Backtester("TSLA")
    #x = tsla.get_bollinger_bands_for_date("10-07-2020", 20)
    #x = tsla.get_bollinger_band_for_date("10-07-2020", 20)

    x = tsla.get_bollinger_band_time_period(20)
    print(x)
