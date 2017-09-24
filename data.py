# import pandas as pd
import quandl, math
import numpy as np

from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = 'ctpB4zaFMD6pTsJEZqwy'

df = quandl.get('WIKI/GOOGL')

# Filter out the rows

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# Calculating some percentage

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

# Filter out rows again

df = df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

forcast_col = 'Adj. Close'

df.fillna(-99999, inplace=True)

forcast_out = int(math.ceil(0.01 * len(df)))

df['label'] = df[forcast_col].shift(-forcast_out)
df.dropna(inplace=True)

# print(df.tail())

X = np.array(df.drop(['label'], 1))

y = np.array(df['label'])

X = preprocessing.scale(X)

# X = X[:-forcast_out + 1]

# df.dropna(inplace=True)

y = np.array(df['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = LinearRegression(n_jobs=-1)

clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)

print(accuracy)