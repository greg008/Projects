# add libs
import pandas
import numpy as np
# read data

cols = ['date', 'price']
df = pandas.read_csv('data.csv', sep=',', names=cols, header=None)
print(df.head())
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

# przygotowanie modelu
from sklearn import linear_model
regr = linear_model.LinearRegression()
print(regr)

# trenowanie modelu
regr.fit(X_train, y_train)

# prediction
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


