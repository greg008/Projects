"""
    WhenShouldiBuy - analyze and predict after how many days
    from premiere of mobile phone price is drop to80% from start price
    Historical Price data are from https://pricespy.co.uk.
    Prices are in British pounds.
    Polynomial regression is used
    7 price ranges is used
"""


import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

import web_price_scraping as wps
import draw_charts as dc
import real_predict as rp


def collecting_data(source_of_data):
    """Scraping data from website or download database and create dataset"""
    scrap_data_obj = wps.ScrapData(source_of_data)
    links = scrap_data_obj.read_links()
    scrap_data_obj.price_scraping(links)
    scrap_data_obj.create_final_dataset()


def poly_and_lin_regression():
    """machine learning, polynomial and linear regression"""
    # Importing the dataset
    dataset = pd.read_csv('data/out_concat.csv')
    x_data = dataset.iloc[:, [1, 4]].values
    y_data = dataset.iloc[:, 3].values

    # Split data
    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data,
                                                        test_size=0.2,
                                                        random_state=0)

    # fit linear regression model
    lin_regr = LinearRegression()
    lin_regr.fit(x_data, y_data)

    # fit Polynomial Regression model
    poly_reg = PolynomialFeatures(degree=2)
    x_poly = poly_reg.fit_transform(x_data)
    poly_reg.fit(x_poly, y_data)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(x_poly, y_data)

    # draw graphs
    dc.grid_of_subplots(dataset, lin_reg_2, poly_reg)

    # Results:
    y_pred = lin_reg_2.predict(poly_reg.fit_transform(x_test))
    print('a=', lin_reg_2.coef_)
    print('b=', lin_reg_2.intercept_)

    # RMSE
    print('RMSERMSE of polynomial regression is', mean_squared_error(y_test,
                                                                     y_pred))

    # R^2
    print('R2 of polynomial regression is', r2_score(y_test, y_pred))

    return poly_reg, lin_reg_2


def comparing_predictions(poly_reg, lin_reg_2):
    """comparing real predictions vs predictions from polynomial regressions"""
    # Predicting a new result with Polynomial Regression
    print(lin_reg_2.predict(poly_reg.fit_transform([[40, 3]])))
    # result [327.40021005]
    # should  be 328.3

    # real prediction no_1
    # 'https://pricespy.co.uk/phones-gps/mobile-phones/
    # samsung-galaxy-note-4-duos-sm-n9100-16gb--p2905869/statistics'
    start_price_1 = 528
    goal_price = int(start_price_1 * 0.8)
    pred_day = 152
    y_pred_all = rp.real_prediction(start_price_1,
                                    lin_reg_2,
                                    poly_reg,
                                    'samsung-galaxy-note-4-duos-sm-n9100')
    dc.real_prediction_plot('Samsung-Galaxy-Note-4',
                            y_pred_all,
                            pred_day,
                            goal_price)

    # 152 day is 80 % to: 422
    # after 152 day from graph is 483 so is 10% fail and

    # real prediction 2
    # 'https://pricespy.co.uk/phones-gps/mobile-phones/
    # sony-xperia-xz1-compact-g8441--p4433342/statistics'
    start_price_2 = 479
    goal_price = int(start_price_2 * 0.8)
    pred_day = 90
    y_pred_all = rp.real_prediction(start_price_2,
                                    lin_reg_2,
                                    poly_reg,
                                    'Sony Xperia XZ1 Compact G8441')
    dc.real_prediction_plot('Sony-Xperia-xz1',
                            y_pred_all,
                            pred_day,
                            goal_price)

    # 90 day is 80 % to: 382
    # after 90 day from graph is 394 so is 4% fail and


def main():
    """main function"""
    collecting_data('database')
    poly_reg, lin_reg_2 = poly_and_lin_regression()
    comparing_predictions(poly_reg, lin_reg_2)


if __name__ == '__main__':
    main()
