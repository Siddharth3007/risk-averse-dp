import yfinance as yf
import numpy as np
import pandas as pd
from radp.config.settings import tickers, historical_period

price_data = yf.download(tickers, period=historical_period, auto_adjust = False, progress = False)
price_data = price_data.reindex(tickers, level = 1, axis = 1) # Reindexing to match the ticker order in yf dataset with desired order
price_data = price_data['Adj Close'].dropna()
rets = np.log(price_data/price_data.shift(1))
rets = rets.dropna()
filename = './data/processed/rets_{0}_{1}_{2}.xlsx'.format(tickers[0], tickers[1], \
                                                                   historical_period)
with pd.ExcelWriter(filename) as writer:
    rets.to_excel(writer)

