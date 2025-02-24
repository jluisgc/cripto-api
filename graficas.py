from binance import Client
from datetime import date, timedelta

import pandas as pd
import mplfinance as mpl



today = date.today()
yesterday = today - timedelta(days=1)
dataticker = "RAYUSDT"
api_key = ""
api_secret = ""

client = Client(api_key, api_secret)
price = client.get_symbol_ticker(symbol=dataticker)
print(price)

asset = dataticker
start = "2025.01.01"
end = str(yesterday)
timeframe = "1d"
df = pd.DataFrame(client.get_historical_klines(asset, timeframe, start, end))
df = df.iloc[:,:6]
df.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]
df = df.set_index("Date")
df.index = pd.to_datetime(df.index, unit="ms")
df = df.astype("float")
print(df)


mpl.plot(df, type='candle', savefig='data/grafica.png')
