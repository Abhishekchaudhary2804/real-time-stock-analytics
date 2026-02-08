import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Stock Dashboard", layout="wide")

st.title("📈 Real-Time Stock Analytics Dashboard")

symbol = st.text_input("Enter Stock Symbol", "AAPL")

API_URL = "http://127.0.0.1:8000"

if st.button("Load Data"):

    stock_resp = requests.get(f"{API_URL}/stock/{symbol}")
    signal_resp = requests.get(f"{API_URL}/signals/{symbol}")

    df = pd.DataFrame(stock_resp.json())
    signals = signal_resp.json()

    st.subheader("Latest Signals")
    st.write(signals)

    fig = go.Figure(data=[
        go.Candlestick(
            x=df["timestamp"],
            open=df["open"],
            high=df["high"],
            low=df["low"],
            close=df["close"]
        )
    ])

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Indicator Table")
    st.dataframe(df.tail(20))
