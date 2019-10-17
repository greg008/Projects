# add libs
import csv
import pandas

# read data for H p9 Lite
cols = ['date', 'price', 'premium', 'name']
df1 = pandas.read_csv('out1.csv', sep=',', names=cols, header=None)
print('head:', df1.head())
print('len:', len(df1))
print('rozmiar', df1.shape)
print('\n')
# convert data to integer(number of days from begining)
df1.insert(0, 'Day', range(0, len(df1)))
print('head:', df1.tail())

# read data for Samsung Galaxy S9
cols = ['date', 'price', 'premium', 'name']
df2 = pandas.read_csv('out2.csv', sep=',', names=cols, header=None)
print('head:', df2.head())
print('len:', len(df2))
print('rozmiar', df2.shape)
print('\n')
# convert data to integer(number of days from begining)
df2.insert(0, 'Day', range(0, len(df2)))
print('head:', df2.tail())

# concenate two dataframes
df3 = pandas.concat([df1, df2], ignore_index=True)
print(df3.head())
print(df3.tail())


# save concat df to csv
pandas.DataFrame(df3).to_csv('out_concat.csv', header=False, quoting=csv.QUOTE_NONE)
print('function finished')

# split data
from sklearn.model_selection import train_test_split
# print(type(df3))
X_data = df3.iloc[:, [0, 3]]
# print(X_data.head())
y_data = df3.iloc[:, 2]
# print(y_data.head())

X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, random_state=1)

# przygotowanie modelu
from sklearn import linear_model
regr = linear_model.LinearRegression()

#trenowanie modelu
regr.fit(X_train, y_train)
print(regr)
# predykcja na danych testowych
y_pred = regr.predict(X_test)
print(y_pred)

print('===Results===')
from sklearn.metrics import mean_squared_error
# results
print('a=', regr.coef_)
print('b=', regr.intercept_)
# mean_squared_error
print('mean_squared_error', mean_squared_error(y_test, y_pred))
#  R^2
print('R^2', regr.score(X_train, y_train))
