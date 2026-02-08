from fastapi import FastAPI
from app.fetcher import fetch_intraday
from app.database import save_to_db
from app.database import get_data
from app.analytics import add_indicators
from app.signals import generate_signals
from app.database import create_signal_table,create_table

app = FastAPI()

create_table()
create_signal_table()


@app.get("/")
def home():
    return {"message": "Stock Analytics API Running"}


@app.get("/stock/{symbol}")
def get_stock(symbol: str):

    symbol = symbol.upper()

    df = get_data(symbol)

    # If stock not in DB → fetch and save
    if df.empty:
        live = fetch_intraday(symbol)
        save_to_db(live)
        df = get_data(symbol)

    df = add_indicators(df)

    return df.tail(100).to_dict(orient="records")

@app.get("/signals/{symbol}")
def get_signals(symbol: str):

    symbol = symbol.upper()

    df = get_data(symbol)

    if df.empty:
        live = fetch_intraday(symbol)
        save_to_db(live)
        df = get_data(symbol)

    df = add_indicators(df)

    return generate_signals(df)

