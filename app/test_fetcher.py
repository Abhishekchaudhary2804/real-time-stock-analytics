from fetcher import fetch_intraday

symbols = ["AAPL", "MSFT", "GOOGL"]

for s in symbols:
    df = fetch_intraday(s)
    print(s)
    print(df.tail())
