import yfinance as yf
import pandas as pd
import json, requests


def sp500():
    sp500df = yf.Ticker("^GSPC").history(period="1y")
    sp500df.to_csv("sp500.csv")
    print(sp500df)
    print("Extraction finisehd sp500")

def gold():
    gold = yf.Ticker("GC=F").history(period="1y")
    gold.to_csv("sp500.csv")
    print(gold)
    print("Extraction finisehd gold")

sp500()
gold()


gold = json.loads(requests.get("https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/XAU/USD").text)
data = gold[0]
dataclean = data["spreadProfilePrices"]
datafinish = dataclean[0]["ask"]
print(str(datafinish))
