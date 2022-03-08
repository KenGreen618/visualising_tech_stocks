import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime
import pandas_datareader.data as web


symbols = ['MSFT', 'AMZN', 'AAPL', 'GOOG', 'FB']
start_date = datetime(2019, 1, 1)
end_date = datetime(2019, 7, 1)

stock_data = web.get_data_yahoo(symbols, start_date, end_date)

adj_close_df = stock_data['Adj Close']
print(adj_close_df)

stock_returns_df = adj_close_df.pct_change()
stock_returns_df.plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("Tech Stocks Returns")
plt.figure(figsize=(16,9))
plt.show()


adj_close_df.plot()
plt.ylabel("Adjusted Closing Price Over Time")
plt.xlabel("Date")
plt.title("Tech Stocks Adjusted Price")
plt.legend()
plt.show()


# subplots
plt.figure(figsize=(15,15))
plt.subplot(3,2,1)
stock_returns_df['MSFT'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("MSFT Returns")

plt.subplot(3,2,2)
stock_returns_df['AMZN'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("AMZN Returns")

plt.subplot(3,2,3)
stock_returns_df['AAPL'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("AAPL Returns")

plt.subplot(3,2,4)
stock_returns_df['GOOG'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("GOOG Returns")

plt.subplot(3,2,5)
stock_returns_df['FB'].plot()
plt.ylabel("Returns Over Time")
plt.xlabel("Date")
plt.title("FB Returns")

plt.subplots_adjust(wspace=0.35, hspace=0.65)
plt.show()