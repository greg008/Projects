import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import sys
sys.path.append("..")
from ML_2 import fromCsvToDf
from ML_2 import prep_and_learn_model

df_concat = fromCsvToDf('out2.csv')
X_data = df_concat.iloc[:, 0]
y_data = df_concat.iloc[:, 2]


plt.scatter(X_data, y_data, color='red')
# plt.plot(X, lin_regr.predict(X), color='blue')
plt.title('mobile price from raw data')
plt.xlabel('Day')
plt.ylabel('Price')
plt.show()


df_concat2 = fromCsvToDf('out2.csv', 'out3.csv', 'out4.csv', 'out5.csv', 'out6.csv', 'out7.csv', 'out8.csv')
prep_and_learn_model(df_concat)




