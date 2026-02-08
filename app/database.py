from sqlalchemy import create_engine, text
import pandas as pd

DB_URL = "sqlite:///app/stocks.db"

engine = create_engine(DB_URL, echo=False)


# ---------- STOCK DATA TABLE ----------

def create_table():
    query = text("""
    CREATE TABLE IF NOT EXISTS stock_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume REAL,
        symbol TEXT
    )
    """)

    with engine.begin() as conn:
        conn.execute(query)


def save_to_db(df):

    if "Datetime" in df.columns:
        df = df.rename(columns={"Datetime": "timestamp"})

    df[["timestamp","open","high","low","close","volume","symbol"]].to_sql(
        "stock_data",
        engine,
        if_exists="append",
        index=False
    )


def get_data(symbol):
    query = f"SELECT * FROM stock_data WHERE symbol='{symbol}'"
    return pd.read_sql(query, engine)


# ---------- SIGNAL HISTORY TABLE ----------

def create_signal_table():
    query = text("""
    CREATE TABLE IF NOT EXISTS signal_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        symbol TEXT,
        signal TEXT,
        reason TEXT
    )
    """)

    with engine.begin() as conn:
        conn.execute(query)


def save_signal(timestamp, symbol, signal, reason):

    df = pd.DataFrame([{
        "timestamp": timestamp,
        "symbol": symbol,
        "signal": signal,
        "reason": reason
    }])

    df.to_sql("signal_history", engine, if_exists="append", index=False)
