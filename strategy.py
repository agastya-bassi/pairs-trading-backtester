import pandas as pd
import numpy as np
from scipy import stats
import yfinance as yf

def fetch_data(ticker1, ticker2, start_date, end_date):
    data = yf.download([ticker1, ticker2], start=start_date, end=end_date)['Close']
    data.columns = [ticker1, ticker2]
    return data.dropna()

def calculate_spread(data, ticker1, ticker2):
    slope, intercept, r, p, se = stats.linregress(data[ticker2], data[ticker1])
    data['Spread'] = data[ticker1] - slope * data[ticker2]
    data['ZScore'] = (data['Spread'] - data['Spread'].mean()) / data['Spread'].std()
    return data, slope, r

def generate_signals(data, threshold):
    data['Signal'] = 0
    data.loc[data['ZScore'] > threshold, 'Signal'] = -1
    data.loc[data['ZScore'] < -threshold, 'Signal'] = 1
    data['SpreadReturn'] = data['Spread'].pct_change()
    data['StrategyReturn'] = data['Signal'].shift(1) * data['SpreadReturn']
    data['CumulativeReturn'] = (1 + data['StrategyReturn']).cumprod()
    return data