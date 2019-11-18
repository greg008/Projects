
"""
        This module implements web scraping functionality
        using https://pricespy.co.uk/phones-gps/mobile-phones
        to create datasets from statistics specific mobile phones
"""

import re
import os
import csv
import sys
sys.path.append("..")

from urllib.request import urlopen
from bs4 import BeautifulSoup
import itertools
import pandas as pd

import utils as ut


def csv_to_df(*args):
    df0 = pd.DataFrame()
    for arg in args:
        cols = ['date', 'price', 'premium', 'name']
        df = pd.read_csv(arg, sep=',', names=cols, header=None)
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

def price_scraping(links):
    for link in links:
        page = urlopen(link)
        soup = BeautifulSoup(page, 'html.parser')
        str_soup = str(soup)

        pattern = re.compile(
            '\"statistics\"\:\{\"pageInfo\"\:\{\"lowestPrice\"\:.*nodes\"\:\[(.*)\]\}\,\"priceForecast',
            re.MULTILINE)
        data = re.findall(pattern, str_soup)
        pattern_name = re.compile('\"Product\",\"name\":\"(.*)\",\"description\":\"Price history', re.MULTILINE)
        data_name = re.findall(pattern_name, str_soup)

        # remove chars
        raw_text = data[0]
        chars = ['{', '}', '"date":', '"lowestPrice":', '"']

        for c in chars:
            raw_text = raw_text.replace(c, "")
        split_text = raw_text.split(',')

        # convert list to dictionary
        list_to_dict = dict(itertools.zip_longest(*[iter(split_text)] * 2, fillvalue=""))

        # create dataframe from dict
        dfObj = pd.DataFrame.from_dict(list_to_dict, orient='index', columns=None)
        dfObj['premium'] = ut.deduce_premium_no(float(dfObj.iloc[3, 0]))

        # add column with name of mobile phone
        dfObj['Phone name'] = data_name[0]
        print(dfObj)

        # create file name
        dir_name = 'data'
        filename_suffix = 'csv'
        base_filename = 'out'
        no_of_file = str(int(ut.deduce_premium_no(float(dfObj.iloc[3, 0]))))

        path = os.path.join(dir_name, no_of_file + base_filename + "." + filename_suffix)

        # write dataframe to csv file
        pd.DataFrame(dfObj).to_csv(path, header=False, quoting=csv.QUOTE_NONE)

# create final csv datafile
def create_final_dataset():
    # concat datasets from various premium number datasets
    df_concat = csv_to_df('data/2out.csv', 'data/3out.csv', 'data/4out.csv', 'data/5out.csv', 'data/6out.csv',
                          'data/7out.csv', 'data/8out.csv')

    # save concat df to csv
    pd.DataFrame(df_concat).to_csv('data/out_concat.csv', header=False, quoting=csv.QUOTE_NONE)
