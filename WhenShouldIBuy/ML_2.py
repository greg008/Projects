# add libs
# https://datatofish.com/multiple-linear-regression-python/
import csv
import pandas
import numpy as np
#

def fromCsvToDf(*names):
    df0 = pandas.DataFrame()
    for name in names:
        print(name)
        cols = ['date', 'price', 'premium', 'name']
        df = pandas.read_csv(name, sep=',', names=cols, header=None)
        df = df.drop(df.index[400:])
        # convert data to integer(number of days from begining)
        df.insert(0, 'Day', range(0, len(df)))
        df_concat = pandas.concat([df0, df], ignore_index=True)
        df0 = df_concat
    return df0

df_concat = fromCsvToDf('out2.csv', 'out3.csv', 'out4.csv', 'out5.csv', 'out6.csv', 'out7.csv', 'out8.csv')

# # save concat df to csv
pandas.DataFrame(df_concat).to_csv('out_concat.csv', header=False, quoting=csv.QUOTE_NONE)
print('function finished')

# split data
from sklearn.model_selection import train_test_split
# print(type(df3))
X_data = df_concat.iloc[:, [0, 3]]
print(X_data.head())
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
new_data_df = pandas.DataFrame([[214, 2]])
y_pred_new = regr.predict(new_data_df)
print('y_pred_new:', y_pred_new)

# predict fall price to 70%

def choose(begining_price):
    if (begining_price <= 300) and (begining_price) >= 200:
        return 2
    elif (begining_price <= 400) and (begining_price) > 300:
        return 3
    elif (begining_price <= 500) and (begining_price) > 400:
        return 4
    elif (begining_price <= 600) and (begining_price) > 500:
        return 5
    elif (begining_price <= 700) and (begining_price) > 600:
        return 6
    elif (begining_price <= 800) and (begining_price) > 700:
        return 7
    elif (begining_price <= 900) and (begining_price) > 800:
        return 8
    else:
        print('none of them')


print('range for begining price 450 is:', choose(450))



# create prediction for specific range

X_specific = pandas.DataFrame()
X_specific.insert(0, 'Day', range(0, 364))
X_specific.insert(1, 'premium', 4)
print('X_specific:', X_specific)


# prediction for specific range
y_pred_specific = regr.predict(X_specific)
print(y_pred_specific)
print(type(y_pred_specific))
print(y_pred_specific.size)


# logic for 80%
percent = 0.8 * 450

for i in range(0, y_pred_specific.size):
    if y_pred_specific[i] <= percent:
        print('80% of begining price will be in:', i, 'day', 'and value is:', y_pred_specific[i])
        break
print(percent)
    # 200 <= begining_price <= 300: 2,
    # 300 < begining_price <= 400: 3,
    # 400 < begining_price <= 500: 4,
    # 500 < begining_price <= 600: 5,
    # 600 < begining_price <= 700: 6,
    # 700 < begining_price <= 800: 7,
    # 800 < begining_price <= 900: 8,

    # return switcher.get(begining_price)

# print('my_switch(250)=', switcher.get(450))

# y_custom_pred = regr.predict(X_test)
# print(y_pred)

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