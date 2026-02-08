import yfinance as yf
import pandas as pd


def fetch_intraday(symbol, period="1d", interval="1m"):
    """
    Fetch intraday stock data using Yahoo Finance
    """

    ticker = yf.Ticker(symbol)
    df = ticker.history(period=period, interval=interval)

    if df.empty:
        raise Exception("No data received")

    df = df.reset_index()

    df = df.rename(columns={
        "Open": "open",
        "High": "high",
        "Low": "low",
        "Close": "close",
        "Volume": "volume",
        "Datetime": "timestamp"
    })

    df["symbol"] = symbol

    return df
