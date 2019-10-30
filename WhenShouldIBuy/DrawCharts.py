import matplotlib.pyplot as plt
import pandas
from sklearn.model_selection import train_test_split
import sys
sys.path.append("..")
from ML_2 import fromCsvToDf
from ML_2 import prep_and_learn_model

df_concat = fromCsvToDf('out2.csv')
X_data = df_concat.iloc[:, 0]
y_data = df_concat.iloc[:, 2]
print(df_concat.shape)
print('xxxxxxxxxxxxxx', df_concat.tail())

plt.plot(X_data, y_data, color='red')
# plt.plot(X, lin_regr.predict(X), color='blue')
plt.title('mobile price from raw data')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()


df_concat2 = fromCsvToDf('out2.csv', 'out3.csv', 'out4.csv', 'out5.csv', 'out6.csv', 'out7.csv', 'out8.csv')
reg = prep_and_learn_model(df_concat)

# create prediction for specific range
X_specific = pandas.DataFrame()
X_specific.insert(0, 'Day', range(0, 364))
X_specific.insert(1, 'premium', 2)
# print('X_specific:', X_specific.head())
# prediction for specific range
y_pred_specific = reg.predict(X_specific)
# print(y_pred_specific)
# print(type(y_pred_specific))
# print(y_pred_specific.size)

X_specific.insert(2, 'Predict_price', y_pred_specific)
print(X_specific.shape)
print(X_specific.tail())
# X_specific.insert(2, 'Predict_price', range(0, 364))


X = X_specific.iloc[:, 0]
y = X_specific.iloc[:, 2]
plt.plot(X_data, y_data, color='red')
plt.plot(X, y, color='blue')
# plt.plot(X, lin_regr.predict(X), color='blue')
plt.title('mobile price from raw data')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()


