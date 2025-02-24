from binance import Client
from datetime import date, timedelta

import pandas as pd
import mplfinance as mpl


dataticker = "RAYUSDT"
api_key = ""
api_secret = ""

client = Client(api_key, api_secret)


#get price
price = client.get_symbol_ticker(symbol=dataticker)

#calculate how much cripto $200 can buy
buy_quantity = round(200 / float(price['price']) )

#create test order
order = client.create_test_order(
    symbol = dataticker,
    side = Client.SIDE_BUY,
    type = Client.ORDER_TYPE_MARKET,
    quantity = buy_quantity
)

#the 200 in buy_quantity is the amount of money you want to spend on the cripto
