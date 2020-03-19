"""
    WhenShouldiBuy - analyze and predict after how many days
    from premiere of mobile phone price is drop to80% from start price
    Historical Price data are from https://pricespy.co.uk.
    Prices are in British pounds.
    Polynomial regression is used
    7 price ranges is used
"""

import sys
sys.path.append("..")

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

import web_price_scraping as wps
import draw_charts as dc
import real_predict as rp
import pandas as pd


def main():
    # Scraping data from website and create dataset
    Scrap_data_obj = wps.ScrapData()
    links = Scrap_data_obj.read_links()
    Scrap_data_obj.price_scraping(links)
    Scrap_data_obj.create_final_dataset()

    # Importing the dataset
    dataset = pd.read_csv('data/out_concat.csv')
    x_data = dataset.iloc[:, [1, 4]].values
    y_data = dataset.iloc[:, 3].values

    # Split data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=0)

    #Feature Scaling
    # from sklearn.preprocessing import StandardScaler
    # sc_X = StandardScaler()
    # X_train = sc_X.fit_transform(X_train)
    # X_test = sc_X.transform(X_test)

    # fit linear regression model
    from sklearn.linear_model import LinearRegression
    lin_regr = LinearRegression()
    lin_regr.fit(x_data, y_data)

    # fit Polynomial Regression model
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree=2)
    x_poly = poly_reg.fit_transform(x_data)
    poly_reg.fit(x_poly, y_data)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(x_poly, y_data)

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

    # real prediction no_1
    # 'https://pricespy.co.uk/phones-gps/mobile-phones/samsung-galaxy-note-4-duos-sm-n9100-16gb--p2905869/statistics'
    start_price_1 = 528
    goal_price = int(start_price_1 * 0.8)
    pred_day = 152
    y_pred_all = rp.real_prediction(start_price_1, lin_reg_2, poly_reg, 'samsung-galaxy-note-4-duos-sm-n9100')
    dc.real_prediction_plot('Samsung-Galaxy-Note-4', y_pred_all, pred_day, goal_price)

    # 152 day is 80 % to: 422
    # after 152 day from graph is 483 so is 10% fail and


    # real prediction 2
    # 'https://pricespy.co.uk/phones-gps/mobile-phones/sony-xperia-xz1-compact-g8441--p4433342/statistics'
    start_price_2 = 479
    goal_price = int(start_price_2 * 0.8)
    pred_day = 90
    y_pred_all = rp.real_prediction(start_price_2, lin_reg_2, poly_reg, 'Sony Xperia XZ1 Compact G8441')
    dc.real_prediction_plot('Sony-Xperia-xz1', y_pred_all, pred_day, goal_price)

    # 90 day is 80 % to: 382
    # after 90 day from graph is 394 so is 4% fail and

if __name__=='__main__':
    main()
