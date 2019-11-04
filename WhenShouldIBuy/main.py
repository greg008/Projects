import sys
sys.path.append("..")
import WebPriceScraping
import pandas as pd
import matplotlib.pyplot as plt

# import Polynomial

def main():
    # Scrap data from website
    links = WebPriceScraping.read_links()
    WebPriceScraping.priceScraping(links)
    WebPriceScraping.concat_data()



    # Reading and preparing the data

    # Regression Learn model

    # Results

    # plot




if __name__=='__main__':
    main()
