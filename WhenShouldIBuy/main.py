import sys
sys.path.append("..")

import WebPriceScraping as wps
import DrawCharts as dc
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Scrap data from website
    links = wps.read_links()
    wps.price_scraping(links)
    wps.concat_data()

    # Importing the dataset
    dataset = pd.read_csv('data/out_concat.csv')
    X = dataset.iloc[:, [1, 4]].values
    Y = dataset.iloc[:, 3].values

    # Split data and Feature Scaling
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)

    # linera regression
    from sklearn.linear_model import LinearRegression
    lin_regr = LinearRegression()
    lin_regr.fit(X, Y)

    # Fitting Polynomial Regression to the dataset
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree=2)
    X_poly = poly_reg.fit_transform(X)
    poly_reg.fit(X_poly, Y)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, Y)

    # plot
    dc.plot_charts(dataset, lin_reg_2, poly_reg)

if __name__=='__main__':
    main()
