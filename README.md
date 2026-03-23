# Pairs Trading Backtester

An interactive quantitative trading tool that backtests z-score mean reversion strategies across any stock pair.

## What is Pairs Trading?
When two historically correlated stocks diverge in price, you buy the cheap one and short the expensive one — betting they'll converge. This tool identifies those moments and simulates the returns.

## How it Works
- Fetches historical price data via yfinance
- Calculates hedge ratio using linear regression
- Computes spread and z-score to identify entry signals
- Backtests the strategy and reports performance metrics

## Key Findings
- **GLD/SLV** at z-score threshold 1.1 produced the best risk-adjusted returns — Sharpe 1.04, Max Drawdown -8.5%
- **XOM/CVX** had the highest correlation (0.97) but lower Sharpe — high correlation alone doesn't guarantee a better trade
- Sweet spot is high correlation AND sufficient spread volatility

## Metrics
- Total Return
- Sharpe Ratio
- Max Drawdown
- Total Trades

## Stack
Python · yfinance · Pandas · NumPy · Scipy · Streamlit · Plotly

## Project Structure
```
app.py        # Streamlit UI and chart rendering
strategy.py   # Spread calculation, z-score, signal generation
utils.py      # Performance metrics
```

## Usage
```bash
pip install -r requirements.txt
streamlit run app.py
```