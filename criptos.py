from datetime import date, timedelta
import pandas as pd
from binance import Client


today = date.today()
yesterday = today - timedelta(days=1)


def criptodata(dataticker):
    api_key = "ez1Oe4LKTrIR0gT0BkwvP5ynjYM2nap400THUIZbhAbz4azcyPkEtdgHG1or4Wn0"
    api_secret = "ogtJZtCEJHkn75MfcmYSj6mcKsxQPRwsBHnQACTdgjjCt9OUeWrC1cmp2449qrHF"
    client = Client(api_key, api_secret)
    price = client.get_symbol_ticker(symbol=dataticker)
    print(price)
    asset = dataticker
    start = "2025.01.01"
    end = str(yesterday)
    timeframe = "1d"
    df = pd.DataFrame(client.get_historical_klines(asset, timeframe, start, end))
    df = df.iloc[:,:6]
    df.columns = ["Date", "Open", "High", "Low", "Close", "Volumen"]
    df = df.set_index("Date")
    df.index = pd.to_datetime(df.index, unit="ms")
    df = df.astype("float")
    print(df)
    #save to csv:
    df.to_csv(dataticker + ".csv", encoding="utf-8")
    print("Data extraction finished.")


list = ['RAYUSDT', 'JUPUSDT', 'SOLUSDT']
for i in list:
    criptodata(i)