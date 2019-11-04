# This module implements web scraping functionality
import re
import os
import csv

from urllib.request import urlopen
from bs4 import BeautifulSoup
import itertools

import pandas as pd


def fromCsvToDf(*names):
    df0 = pd.DataFrame()
    for name in names:
        cols = ['date', 'price', 'premium', 'name']
        df = pd.read_csv(name, sep=',', names=cols, header=None)
        df = df.drop(df.index[400:])
        # convert data to integer(number of days from begining)
        df.insert(0, 'Day', range(0, len(df)))
        df_concat = pd.concat([df0, df], ignore_index=True)
        df0 = df_concat
    return df0


# read links and remove newline characters
def read_links():
    with open('data/links.txt') as f:
        links = [link.strip('\n') for link in f]
    return links

# choose premium number from begining price
def choose(begining_price):
    if (begining_price <= 300) and (begining_price) >= 200:
        return 2
    elif (begining_price <= 400) and (begining_price) > 300:
        return 3
    elif (begining_price <= 500) and (begining_price) > 400:
        return 4
    elif (begining_price <= 600) and (begining_price) > 500:
        return 5
    elif (begining_price <= 700) and (begining_price) > 600:
        return 6
    elif (begining_price <= 800) and (begining_price) > 700:
        return 7
    elif (begining_price <= 900) and (begining_price) > 800:
        return 8
    else:
        print('none of them')

# def parse_links(links):


def price_scraping(links):
    for link in links:
        page = urlopen(link)
        soup = BeautifulSoup(page, 'html.parser')
        soup2 = str(soup)

        pattern = re.compile(
            '\"statistics\"\:\{\"pageInfo\"\:\{\"lowestPrice\"\:.*nodes\"\:\[(.*)\]\}\,\"priceForecast',
            re.MULTILINE)
        data = re.findall(pattern, soup2)
        pattern_name = re.compile('\"Product\",\"name\":\"(.*)\",\"description\":\"Price history', re.MULTILINE)
        data_name = re.findall(pattern_name, soup2)
        rm_characters = data[0]
        chars = ['{', '}', '"date":', '"lowestPrice":', '"']

        for c in chars:
            rm_characters = rm_characters.replace(c, "")
        split_data = rm_characters.split(',')

        # convert list to dictionary
        d = dict(itertools.zip_longest(*[iter(split_data)] * 2, fillvalue=""))

        # create dataframe from dict
        dfObj = pd.DataFrame.from_dict(d, orient='index', columns=None)
        dfObj['premium'] = choose(float(dfObj.iloc[3, 0]))

        # add column with name of mobile phone
        dfObj['Phone name'] = data_name[0]
        print(dfObj)

        # create file name
        dir_name = 'data'
        filename_suffix = 'csv'
        base_filename = 'out'
        no_file = str(int(choose(float(dfObj.iloc[3, 0]))))

        path = os.path.join(dir_name, no_file + base_filename + "." + filename_suffix)

        # write dataframe to csv file
        pd.DataFrame(dfObj).to_csv(path, header=False, quoting=csv.QUOTE_NONE)

# create final csv datafile
def concat_data():
    df_concat = fromCsvToDf('data/2out.csv', 'data/3out.csv', 'data/4out.csv', 'data/5out.csv', 'data/6out.csv', 'data/7out.csv', 'data/8out.csv')

    # save concat df to csv
    pd.DataFrame(df_concat).to_csv('data/out_concat.csv', header=False, quoting=csv.QUOTE_NONE)

