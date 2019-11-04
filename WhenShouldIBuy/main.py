import sys
sys.path.append("..")

import web_price_scraping as wps
import draw_charts as dc
import pandas as pd

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

    # podaj cene początkową np 555
    # 'https://pricespy.co.uk/phones-gps/mobile-phones/samsung-galaxy-note-4-duos-sm-n9100-16gb--p2905869/statistics'


    X_data_begining = 528
    premium_no = wps.choose(X_data_begining)
    percent_treshold = int(X_data_begining * 0.8)
    print('X_data_begining:', X_data_begining)
    print('percent_treshold 80%:', percent_treshold)

    x_specific = pd.DataFrame()
    x_specific.insert(0, 'Day', range(0, 364))
    x_specific.insert(1, 'premium', premium_no)
    y_pred_all = lin_reg_2.predict(poly_reg.fit_transform(x_specific))
    print('y_pred_all', y_pred_all)

    for i in range(y_pred_all.size):
        if y_pred_all[i] <= percent_treshold:
            print(i, '80% to: ', y_pred_all[i])
            break
    # 153 day is 80 % to: 421.96564126781067
    # after 153 day from graph is 483 so is 10% fail and

    # logic for 80%
    # percent = 0.8 * 386
    #
    # for i in range(0, y_pred_specific.size):
    #     if y_pred_specific[i] <= percent:
    #         print('80% of begining price will be in:', i, 'day', 'and value is:', y_pred_specific[i])
    #         break
    # print(percent)

    # a= [ 0.00000000e+00 -3.32729696e-01  1.03566759e+02  1.37668444e-03
    #  -1.43230158e-01 -6.98360154e-01]
    # b= 49.57146089318843
    # RMSERMSE of polynomial regression is 1600.6850904251307
    # R2 of polynomial regression is 0.9382259298946103
    # [325.6923847]

    # dla 400
    # a = [0.00000000e+00 - 3.39725836e-01  9.77563618e+01  1.16142115e-03
    #      - 1.28803606e-01 - 3.00586314e-01]
    # b = 64.0235938028398
    # RMSERMSE
    # of
    # polynomial
    # regression is 1734.4589431839693
    # R2
    # of
    # polynomial
    # regression is 0.9333360342522857
    # [327.40021005]


if __name__=='__main__':
    main()
