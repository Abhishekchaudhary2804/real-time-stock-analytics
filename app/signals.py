from app.database import save_signal
from app.alerts import send_alert

def generate_signals(df):

    latest = df.iloc[-1]
    symbol = latest["symbol"]

    signals = []

    if latest["RSI"] < 30:
        signals.append(("BUY","RSI Oversold"))

    if latest["RSI"] > 70:
        signals.append(("SELL","RSI Overbought"))

    if latest["SMA20"] > latest["EMA20"]:
        signals.append(("BUY","SMA crossed EMA"))

    if latest["MACD"] > latest["MACD_signal"]:
        signals.append(("BUY","MACD Bullish"))

    output = []

    for sig, reason in signals:
        save_signal(str(latest["timestamp"]), symbol, sig, reason)
        send_alert(f"{symbol} {sig} — {reason}")
        output.append({
            "timestamp": str(latest["timestamp"]),
            "signal": sig,
            "reason": reason
        })

    return output
