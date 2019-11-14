import sys
sys.path.append("..")

import web_price_scraping as wps
import draw_charts as dc
import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

def main():
    # Scraping data from website
    links = wps.read_links()
    wps.price_scraping(links)
    wps.concat_data()

    # Importing the dataset
    dataset = pd.read_csv('data/out_concat.csv')
    X = dataset.iloc[:, [1, 4]].values
    Y = dataset.iloc[:, 3].values

    # Split data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    #Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc_X = StandardScaler()
    # X_train = sc_X.fit_transform(X_train)
    # X_test = sc_X.transform(X_test)

    # fit linear regression model
    from sklearn.linear_model import LinearRegression
    lin_regr = LinearRegression()
    lin_regr.fit(X, Y)

    # fit Polynomial Regression model
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree=2)
    X_poly = poly_reg.fit_transform(X)
    print('X_poly', X_poly)
    poly_reg.fit(X_poly, Y)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, Y)

    # draw graphs
    dc.grid_of_subplots(dataset, lin_reg_2, poly_reg)

    # Results:
    y_pred = lin_reg_2.predict(poly_reg.fit_transform(X_test))
    print('a=', lin_reg_2.coef_)
    print('b=', lin_reg_2.intercept_)

    # RMSE
    print('RMSERMSE of polynomial regression is', mean_squared_error(y_test, y_pred))

    # R^2
    print('R2 of polynomial regression is', r2_score(y_test, y_pred))

    # Predicting a new result with Polynomial Regression
    print(lin_reg_2.predict(poly_reg.fit_transform([[40, 3]])))
    # result [327.40021005]
    # should  be 328.3

    # % percent

    # real prediction 1
    # 'https://pricespy.co.uk/phones-gps/mobile-phones/samsung-galaxy-note-4-duos-sm-n9100-16gb--p2905869/statistics'

    data_begining = 528
    premium_no = wps.choose(data_begining)
    percent_treshold = int(data_begining * 0.8)
    print('data_begining:', data_begining)
    print('percent_treshold 80%:', percent_treshold)

    x_specific = pd.DataFrame()
    x_specific.insert(0, 'Day', range(0, 364))
    x_specific.insert(1, 'premium', premium_no)
    y_pred_all = lin_reg_2.predict(poly_reg.fit_transform(x_specific))

    print('prediction for samsung-galaxy-note-4-duos-sm-n9100')
    for i in range(y_pred_all.size):
        if y_pred_all[i] <= percent_treshold:
            print('Begining price(', data_begining, ')', ' should drop to 80% (', y_pred_all[i], ')', ' in ', i, 'day')
            break
    # 153 day is 80 % to: 421.96564126781067
    # after 153 day from graph is 483 so is 10% fail and

    dc.real_prediction_plot('Samsung-Galaxy-Note-4', y_pred_all, 152, 421)


    # real prediction 2
    # 'https://pricespy.co.uk/phones-gps/mobile-phones/sony-xperia-xz1-compact-g8441--p4433342/statistics'

    data_begining = 479
    premium_no = wps.choose(data_begining)
    percent_treshold = int(data_begining * 0.8)
    print('data_begining:', data_begining)
    print('percent_treshold 80%:', percent_treshold)

    x_specific = pd.DataFrame()
    x_specific.insert(0, 'Day', range(0, 364))
    x_specific.insert(1, 'premium', premium_no)
    y_pred_all = lin_reg_2.predict(poly_reg.fit_transform(x_specific))

    print('prediction for Sony Xperia XZ1 Compact G8441')
    for i in range(y_pred_all.size):
        if y_pred_all[i] <= percent_treshold:
            print('Begining price(', data_begining, ')', ' should drop to 80% (', y_pred_all[i], ')', ' in ', i, 'day')
            break
    # 90 day is 80 % to: 382
    # after 90 day from graph is 394 so is 4% fail and

    dc.real_prediction_plot('Sony-Xperia-xz1', y_pred_all, 90, 382)

if __name__=='__main__':
    main()
