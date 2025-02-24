import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer

# Load data
btc_data = pd.read_csv("data/JUPUSDT.csv").tail(30)
eth_data = pd.read_csv("data/RAYUSDT.csv").tail(30)

# Preprocessing
btc_data.dropna(inplace=True)
eth_data.dropna(inplace=True)

# Shift the "Close" column of "BTCUSDT.csv" by one day
btc_data['Close'] = btc_data['Close'].shift(1)

# Merge the two dataframes on the "Date" column
merged_data = pd.merge(btc_data[['Date', 'Close']], eth_data[['Date', 'Close']], on='Date', how='inner')

# Split data into training and testing sets
train_data = merged_data.iloc[:-1, :]
test_data = merged_data.iloc[-1:, :]

# Impute missing values using the mean
imputer = SimpleImputer(strategy='mean')
train_predictors = imputer.fit_transform(train_data.iloc[:, 1].values.reshape(-1, 1))
test_predictors = imputer.transform(test_data.iloc[:, 1].values.reshape(-1, 1))

# Fit the linear regression model
regression = LinearRegression()
regression.fit(train_predictors, train_data.iloc[:, 2].values.reshape(-1, 1))

# Predict the close price of "JUPUSDT.csv"
predicted_price = regression.predict(test_predictors)

# Check if the price is going to go up or down
if predicted_price > test_data.iloc[0, 2]:
    print("The price of JUPUSDT is predicted to go up.")
    
else:
    print("The price of JUPUSDT is predicted to go down.")