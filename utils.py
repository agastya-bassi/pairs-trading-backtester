import numpy as np

def calculate_metrics(data):
    total_return = data['CumulativeReturn'].iloc[-1] - 1
    sharpe = data['StrategyReturn'].mean() / data['StrategyReturn'].std() * np.sqrt(252)
    rolling_max = data['CumulativeReturn'].cummax()
    drawdown = (data['CumulativeReturn'] - rolling_max) / rolling_max
    max_drawdown = drawdown.min()
    total_trades = int((data['Signal'].diff() != 0).sum())
    return total_return, sharpe, max_drawdown, total_trades