import yfinance as yf
import pandas as pd

# Download historical data for AAPL
data = yf.download("AAPL", start="2022-01-01", end="2023-12-31", interval="1d")

# Preview
print(data.head())