from fetcher import fetch_intraday
from database import create_table, save_to_db, get_data

create_table()

df = fetch_intraday("AAPL")

save_to_db(df)

data = get_data("AAPL")

print(data.tail())
