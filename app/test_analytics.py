from app.database import get_data
from app.analytics import add_indicators


df = get_data("AAPL")

df = add_indicators(df)

print(df[["timestamp","close","SMA20","EMA20","RSI","MACD"]].tail())
