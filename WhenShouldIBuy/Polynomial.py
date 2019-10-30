# Polynomial Regression

import sys
sys.path.append("..")
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('out_concat.csv')
print(dataset.tail())
X = dataset.iloc[:, [1, 4]].values
Y = dataset.iloc[:, 3].values
print(X)
# y = dataset.iloc[:, 2].values

# Feature Scaling
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state = 0)
print(X_train)
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
print(X_train)

# wybranie i uczenie modelu regresji liniowej
from sklearn.linear_model import LinearRegression
lin_regr = LinearRegression()
lin_regr.fit(X, Y)


# Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X)
print('X_poly', X_poly)
poly_reg.fit(X_poly, Y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, Y)

# wizualizacja regresji wielomianowej
import matplotlib.pyplot as plt
# plt.plot(X, Y, color='red')
# plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color='blue')
# plt.title('Truth or Bluff (Polynomial Regression)')
# plt.xlabel('Position level')
# plt.ylabel('Salary')
# plt.show()


mainDf = dataset[dataset.iloc[:, 4] == 2]
print('maindf = ', mainDf)
print(mainDf.shape)
y_raw = mainDf.iloc[0:364, 3]
# print('y_raw', y_raw)

def draw_plot_polynomial(premium_no):
    X_specific = pd.DataFrame()
    X_specific.insert(0, 'Day', range(0, 364))
    X_specific.insert(1, 'premium', premium_no)
    # y_raw =
    y = lin_reg_2.predict(poly_reg.fit_transform(X_specific))
    # print('predict for ', premium_no, '=', y)
    plt.plot(range(0, 364), y_raw)
    plt.plot(range(0, 364), y, color='blue')
    plt.show()

draw_plot_polynomial(2)

# Predicting a new result with Polynomial Regression
# print(lin_reg_2.predict(poly_reg.fit_transform([[100, 7]])))
