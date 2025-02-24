import pandas as pd
import numpy as np


#select csv últimos 30 datos
sp500_df = pd.read_csv("data/sp500.csv").tail(30)
gold_df = pd.read_csv("data/gold.csv").tail(30)

#columns for study
sp500_prices = sp500_df[["Date", "Close"]]
gold_prices = gold_df[["Date", "Close"]]

#fusion in a dame dataframe
df = pd.merge(sp500_prices, gold_prices, on="Date", how="inner")

#correlation
correlation = np.corrcoef(df["Close_x"], df["Close_y"])[0,1]
print(correlation)

# asignar una puntuación basada en el nivel de correlación
if correlation > 0.8:
    score = 10
elif correlation > 0.78:
    score = 9
elif correlation > 0.4:
    score = 8
elif correlation > 0.2:
    score = 7
elif correlation > 0:
    score = 6
elif correlation > -0.2:
    score = 5
elif correlation > -0.4:
    score = 4
elif correlation > -0.6:
    score = 3
elif correlation > -0.8:
    score = 2
else:
    score = 1

# imprimir la puntuación
print(f"La puntuación de correlación entre sp500 y oro es: {score}")