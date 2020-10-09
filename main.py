import pandas as pd
import numpy as nd
import yfinance as yf
from signals import Signals as sign


class Backtester:

    def __init__(self, ticker):
        self.ticker = yf.Ticker(ticker)
        self.hist = self.ticker.history(period="max")
        self.hist.reset_index(inplace=True)

    # Returns Simple Moving Average for a specific date
    def get_sma_for_date(self, date, smatype):
        s = sign(self.ticker)

        return s.sma(self.hist, smatype, date)

    # Returns list of Simple Moving Averages for a interval of trading days

    def get_sma_time_period(self, window):
        dates_and_sma = []
        for date in self.hist["Date"][- window:]:
            dates_and_sma.append((date, self.get_sma_for_date(date, window)))

        return dates_and_sma

    def get_ema_for_date(self, date, ematype):
        s = sign(self.ticker)

        return s.ema(self.hist, ematype, date)

    # Returns Bollinger bands for a specific date
    def get_bollinger_bands_for_date(self, date, bollingertype):
        s = sign(self.ticker)

        return s.bollinger_bands(self.hist, bollingertype, date)

    # Returns a list of tuple, with date, upper and lower Bollinger Bands
    def get_bollinger_band_time_period(self, window):
        dates_and_bollinger_bands = []
        for date in self.hist["Date"][- window:]:
            dates_and_bollinger_bands.append(
                (date, self.get_bollinger_bands_for_date(date, window)))

        return dates_and_bollinger_bands

    # Returns full lenght of ticker history percentage changes from previous Closed Price
    def get_pct_change(self):
        s = sign(self.ticker)
        return s.pct_change(self.hist)


if __name__ == "__main__":
    tsla = Backtester("TSLA")
    #x = tsla.get_bollinger_bands_for_date("10-07-2020", 20)
    #x = tsla.get_bollinger_band_for_date("10-07-2020", 20)
    #x = tsla.get_bollinger_band_time_period(20)
    #x = tsla.get_pct_change()
    x = tsla.get_ema_for_date("10-08-2020", 50)
    print(x)
