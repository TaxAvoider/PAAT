"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Portfolio Allocation Assist Tool
PAAT

Create by Harrison Langdon on 16/11/2021

v0.1
Will assist in portfolio diversity
May be expanded to hold more functions
For now only contains correlation
Purpose of program is to display the correlation of two given securities.
"""


import math
import numpy as np
import pandas
import matplotlib.pyplot as plt
import yfinance as yf
import statistics

# market_base = yf.download("BTC-AUD", period="30d", interval="1d")

def get_data():
    # data = yf.Ticker('GOOG')
    # eth = yf.Ticker("ETH-AUD").history(period=str("1") + "y")

    data = yf.download("ETH-AUD", period="30d", interval="1d")
    return data


def stock(ticker, time_period, interval):
    print("Please enter your desired stock ticker, time period and interval")
    print('Examples for tickers include:'
          '"Goog"       Google'
          '"BTC-AUD"    Bitcoin in Australian Dollars')
    print('Examples for time period include:'
          '"200d"       200 days of price history'
          '"48h"        48 hours of price history'
          '"30m"        30 minutes of price history')
    print('Examples for time intervals:'
          '"1d"         Interval of daily price data'
          '"1h"         Interval of hourly price data'
          '"15m         Interval of 15 minute price data (Smallest unit for price data)')
    try:
        return yf.download(ticker, period=time_period, interval=interval)
    except:
        return "Error in downloading stock price data"


def graph(sec_data):
    plt.plot(sec_data)
    plt.show()
    return 0


def beta(market, sec_b):
    print(f"Market: {market:^10}")
    print(f"sec_b: {sec_b:^10}")
    # Converts data of sec_a into
    market = yf.download(market, period="5y", interval="1mo")
    sec = yf.download(sec_b, period="5y", interval="1mo")

    sec_a = market["Close"].to_numpy()
    sec_b = sec["Close"].to_numpy()

    print(sec_a.shape)
    print(sec_b.shape)

    #sec_a.to_numpy()
    #sec_b.to_numpy()

    # Covariance map
    #cov_map = np.stack((sec_a, sec_b), axis=0)
    #cov = np.cov(cov_map)

    var = statistics.variance(sec_a)

    cov = np.cov(sec_a, sec_b)
    # var = cov[0][0]
    print(cov)
    # Gets the covariance out of the covariance matrix
    cov = cov[0][1]

    print("---------------------------------------------")
    print(f"beta is: {var/cov}")
    print("_____________________________________________")

    return 0


def main():
    coins = ['BTC', 'ETH', 'BNB', 'XRP', 'USDT', 'DOGE', 'ADA', 'BCH', 'LTC', 'LINK',
             'USDC', 'XLM', 'VET', 'ETC', 'EOS', 'TRX']
    #for i in range(len(coins)):
        #beta("BTC-AUD", coins[i]+"-AUD")
    beta("SPY", "GOOG")
    #beta("BTC-AUD", "ETH-AUD")


if __name__ == '__main__':
    main()
    print("End of program")

