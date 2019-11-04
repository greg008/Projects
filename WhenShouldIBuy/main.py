import sys
sys.path.append("..")

import web_price_scraping as wps
import draw_charts as dc
import pandas as pd


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
    from sklearn.preprocessing import StandardScaler
    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)

    # fit linear regression model
    from sklearn.linear_model import LinearRegression
    lin_regr = LinearRegression()
    lin_regr.fit(X, Y)

    # fit Polynomial Regression model
    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures(degree=2)
    X_poly = poly_reg.fit_transform(X)
    poly_reg.fit(X_poly, Y)
    lin_reg_2 = LinearRegression()
    lin_reg_2.fit(X_poly, Y)

    # draw graphs
    dc.grid_of_subplots(dataset, lin_reg_2, poly_reg)

if __name__=='__main__':
    main()
