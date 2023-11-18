import os

import pandas as pd

DIVIDEND_PATH = "context/raw/dividends"
PRICES_PATH = "context/raw/prices"

dividend_data = []
prices_data = []

for file in os.listdir(DIVIDEND_PATH):
    ticker = file.split(".")[0]
    _div_data = pd.read_csv(os.path.join(DIVIDEND_PATH, file))
    _prices_data = pd.read_csv(os.path.join(PRICES_PATH, file))

    _div_data.loc[:, "Ticker"] = ticker
    _prices_data.loc[:, "Ticker"] = ticker

    dividend_data.append(_div_data)
    prices_data.append(_prices_data)

dividend_df = pd.concat(dividend_data)
prices_df = pd.concat(prices_data)

dividend_df.to_csv("context/processed_data/dividends.csv", index=False)
prices_df.to_csv("context/processed_data/prices.csv", index=False)