from app.database import get_data
from app.analytics import add_indicators
from app.signals import generate_signals

df = get_data("AAPL")
df = add_indicators(df)

latest = df.iloc[-1]

print("Latest RSI:", latest["RSI"])
print("SMA20:", latest["SMA20"])
print("EMA20:", latest["EMA20"])
print("MACD:", latest["MACD"])
print("MACD Signal:", latest["MACD_signal"])

signals = generate_signals(df)

print("Signals:", signals)
