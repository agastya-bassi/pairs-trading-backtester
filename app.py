import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from strategy import fetch_data, calculate_spread, generate_signals
from utils import calculate_metrics

st.title("Pairs Trading Backtester")
st.sidebar.header("Strategy Settings")

ticker1 = st.sidebar.text_input("Stock 1", value="GLD")
ticker2 = st.sidebar.text_input("Stock 2", value="SLV")
start_date = st.sidebar.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", value=pd.to_datetime("2024-01-01"))
threshold = st.sidebar.slider("Entry Z-Score Threshold", 1.0, 3.0, 2.0, 0.1)

if st.sidebar.button("Run Backtest"):
    data = fetch_data(ticker1, ticker2, start_date, end_date)
    data, slope, r = calculate_spread(data, ticker1, ticker2)
    data = generate_signals(data, threshold)
    total_return, sharpe, max_drawdown, total_trades = calculate_metrics(data)

    st.sidebar.metric("Correlation", f"{r:.2f}")
    st.sidebar.metric("Hedge Ratio", f"{slope:.2f}")

    # Z-Score chart
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=data.index, y=data['ZScore'], name='Z-Score', line=dict(color='cyan')))
    fig1.add_hline(y=threshold, line_dash="dash", line_color="red", annotation_text="Short")
    fig1.add_hline(y=-threshold, line_dash="dash", line_color="green", annotation_text="Long")
    fig1.add_hline(y=0, line_dash="dot", line_color="white")
    fig1.update_layout(title="Spread Z-Score", template="plotly_dark")
    st.plotly_chart(fig1)

    # Cumulative returns chart
    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=data.index, y=data['CumulativeReturn'], name='Strategy', line=dict(color='lime')))
    fig2.add_hline(y=1, line_dash="dash", line_color="white")
    fig2.update_layout(title="Cumulative Strategy Returns", template="plotly_dark")
    st.plotly_chart(fig2)

    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Return", f"{total_return:.1%}")
    col2.metric("Sharpe Ratio", f"{sharpe:.2f}")
    col3.metric("Max Drawdown", f"{max_drawdown:.1%}")
    col4.metric("Total Trades", f"{total_trades}")