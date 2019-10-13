# add libs
import sys
sys.path.append("..")
import WebPriceScraping
import pandas
import numpy as np

# read data
cols = ['date', 'price']
# df = pandas.read_csv('data.csv', sep=',', names=cols, header=None)
df = pandas.read_csv('out1.csv', sep=',', names=cols, header=None)
print(df.head())
print('rozmiar', df.shape)
# convert data to integer(number of days from begining)

df['date'] = pandas.to_datetime(df['date'])
df['date_delta'] = (df['date'] - df['date'].min()) / np.timedelta64(1, 'D')
print(df.head())
# city_data = df[df['city'] == 'London']
# result = sm.ols(formula = 'sales ~ date_delta', data = city_data).fit()
# https://stackoverflow.com/questions/24588437/convert-date-to-float-for-linear-regression-on-pandas-data-frame
# convert the dates or timestamps to an integer number of days since the start of the data

# visualisation of data
import matplotlib as plt
df.plot(x='date_delta', y='price')
# plt.pyplot.show()

# prepare data
from sklearn.model_selection import train_test_split
X_data = df[['date_delta']]
Y_data = df[['price']]
X_train, X_test, y_train, y_test = train_test_split(X_data, Y_data, random_state=1)

# przygotowanie modelu linear regression
from sklearn import linear_model
regr = linear_model.LinearRegression()
print(regr)

# przygotowanie modelu polynomial regression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_regr = PolynomialFeatures(degree=4)
X_poly = poly_regr.fit_transform(X_data)
poly_regr.fit(X_poly, Y_data)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y_data)

# wizualizacja regresji wielomianowej
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
plt.scatter(X_data, Y_data, color='red')
plt.plot(X_data, lin_reg_2.predict(poly_regr.fit_transform(X_data)), color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
# plt.show()
poly_pred = lin_reg_2.predict(poly_regr.fit_transform(X_data))
# print('poly_pred', poly_pred)
rmse = np.sqrt(mean_squared_error(Y_data, poly_pred))
print('RMSE', rmse)
r2 = r2_score(Y_data, poly_pred)
print('R^2', r2)


# trenowanie modelu
regr.fit(X_train, y_train)

# prediction
# print('xxxxxxxxxxxxxxxxx',X_test)
y_pred = regr.predict(X_test)

# results
from sklearn.metrics import mean_squared_error
# chcemy poznac bład sredniokwadratowy, wspólczynniki a i b , wspólczynnik determinacji r^2
# y = ax + b
print("Wspólczynnik a:", regr.coef_)
print("Wyraz wolny b:", regr.intercept_)
print("Bład sredniokwadratowy:", mean_squared_error(y_test, y_pred))
# idealny to = 1 czyli 100 %
print("Wspólczynnik determinacji R^2 :", regr.score(X_train, y_train))

# wizualizacja po
# nakładanie  przewidywanych danych na wykres
import matplotlib.pyplot as plt1
plt1.scatter(X_train, y_train)
plt1.plot(X_test, y_pred, color='red', linewidth=3)
# plt1.show()
# WebPriceScraping.priceScraping()

print('X_train:', X_train['date_delta'])
# print(type('type:', X_train))
print('X train shape', X_train.shape)
# print('y_train:', y_train)
# print('Price after 100 days',)

print('oryginal price after 100 days:', df.loc[200, 'price'])
# print(df.loc[100, ['date_delta']])
# poly_regr.fit(X_poly, Y_data)
X_data_1 = df.loc[200, 'date_delta']
X_data_all = df.loc[:, 'date_delta']
print(X_data_all)
# y_pred = regr.predict(X_test)

# print('X_data_1', X_data_1)
y_pred_100 = regr.predict(X_data_1.reshape(-1, 1))
y_pred_all = regr.predict(X_data_all.values.reshape(-1, 1))
print('model predict price after 100 days:', y_pred_100)
print('model predict all price: ', y_pred_all)

print(type(y_pred_all))
print(y_pred_all.size)

# % percent
X_data_begining = df.loc[0, 'price']
percent_treshold = int(X_data_begining * 0.8)
print('percent_treshold:', percent_treshold)

print('X_data_begining:', X_data_begining)
for i in range(y_pred_all.size):
    if y_pred_all[i] <= percent_treshold:
        print(i, '80% to: ', y_pred_all[i])
        break

# print(df.loc[77, 'price'])
# print(y_pred_all[77])


