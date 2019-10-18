# add libs
# https://datatofish.com/multiple-linear-regression-python/
import csv
import pandas
#
# # read data for Huawei P9 Lite
# cols = ['date', 'price', 'premium', 'name']
# df2 = pandas.read_csv('out2.csv', sep=',', names=cols, header=None)
# print('head:', df2.head())
# print('len:', len(df2))
# print('rozmiar', df2.shape)
# print('\n')
# # convert data to integer(number of days from begining)
# df1.insert(0, 'Day', range(0, len(df2)))
# print('head:', df2.tail())
#
# # read data for Samsung Galaxy S9
# cols = ['date', 'price', 'premium', 'name']
# df3 = pandas.read_csv('out3.csv', sep=',', names=cols, header=None)
# print('head:', df3.head())
# print('len:', len(df3))
# print('rozmiar', df3.shape)
# print('\n')
# # convert data to integer(number of days from begining)
# df2.insert(0, 'Day', range(0, len(df3)))
# print('head:', df3.tail())

def fromCsvToDf(*names):
    df0 = pandas.DataFrame()
    for name in names:
        print(name)
        cols = ['date', 'price', 'premium', 'name']
        df = pandas.read_csv(name, sep=',', names=cols, header=None)
        # convert data to integer(number of days from begining)
        df.insert(0, 'Day', range(0, len(df)))
        df_concat = pandas.concat([df0, df], ignore_index=True)
        df0 = df_concat
    return df0

df_concat = fromCsvToDf('out2.csv', 'out3.csv', 'out4.csv', 'out5.csv', 'out6.csv', 'out7.csv', 'out8.csv')

# # save concat df to csv
pandas.DataFrame(df_concat).to_csv('out_concat.csv', header=False, quoting=csv.QUOTE_NONE)
print('function finished')

# # concenate two dataframes
# df_concat = pandas.concat([df2, df3], ignore_index=True)
# print(df_concat.head())
# print(df_concat.tail())

# split data
from sklearn.model_selection import train_test_split
# print(type(df3))
X_data = df_concat.iloc[:, [0, 3]]
# print(X_data.head())
y_data = df_concat.iloc[:, 2]
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

# predict new data
new_data_df = pandas.DataFrame([[389, 3]])
y_pred_new = regr.predict(new_data_df)
print('y_pred_new:', y_pred_new)
#
# # ===Results=== with only 2 out files
# # a= [-1.41403473e-01  2.58113306e+02]
# # b= 249.69047160325027
# # mean_squared_error 2771.5821833441446
# # R^2 0.8821138445508246
# # y_pred_new: [475.56378528]

# ===Results=== with all 8 out csv files
# a= [-0.22040416 55.73546641]
# b= 168.7123337019193
# mean_squared_error 3521.8681493871045
# R^2 0.8501339566649047