# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

tickers = ['BRL=X', 'BTCUSD=X', 'GLD', 'JPY=X', 'EUR=X']
data = pd.DataFrame()

for t in tickers:
    data[t] = wb.DataReader(name=t, data_source='yahoo', start='2015-1-1', end='2020-5-10')['Adj Close']
    
data['BRL=X'] = data['BRL=X'].fillna(np.mean(data['BRL=X']))
data['BTCUSD=X'] = data['BTCUSD=X'].fillna(np.mean(data['BTCUSD=X']))
data['GLD'] = data['GLD'].fillna(np.mean(data['GLD']))
data['JPY=X'] = data['JPY=X'].fillna(np.mean(data['JPY=X']))


y = data['BRL=X']

x = pd.DataFrame(data['BTCUSD=X'])
x['GLD'] = pd.DataFrame(data['GLD'])
x['JPY'] = pd.DataFrame(data['JPY=X'])
x['EUR'] = pd.DataFrame(data['EUR=X'])

### REGRESSÃO LINEAR

est = sm.OLS(y, x)
est2 = est.fit()
print(est2.summary())

sns.regplot(x['JPY'], y)









