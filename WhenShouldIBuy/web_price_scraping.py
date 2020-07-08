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

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import itertools

import pandas as pd

import utils as ut
import postgre_sql


class ScrapData:
    """The ScrapData web scraper collects data from
        www.https://pricespy.co.uk/phones-gps/mobile-phones
        returned Pandas dataframe with data
    """

    def __init__(self, get_data: str = 'website',
                 url: str = 'https://pricespy.co.uk/phones-gps/mobile-phones/'
                            'honor-10-4gb-ram-128gb--p4802117/statistics',
                 ):
        """Args:
            url (str): full HTML link to a page of pricespy.co.uk.
            website (str): create dataset from website or database
        """

        self.__status_code = self._request(url)
        self.__url = url
        self.__validate_url()
        self._get_data = get_data
        print(self.__status_code)
        print(url)

    @staticmethod
    def _request(url: str):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        open_url = urlopen(req)
        return open_url.getcode()

    def __validate_url(self):
        """Basic url validation."""
        real_url = "{}://pricespy.co.uk/{}/"
        protocols = ["http", "https"]
        words = ["phones-gps/mobile-phones"]
        urls = [real_url.format(p, t) for p in protocols for t in words]
        conditions = [self.url.startswith(u) for u in urls]
        conditions.append(self.__status_code == 200)
        print(conditions)

        # False: Any() returns False if no elements are True.
        # So "not any" is the same as "no True values."
        if not any(conditions):
            raise ValueError(f"Invalid pricespy.co.uk URL:\n\n\t{self.url}")

    @property
    def url(self):
        """url property"""
        return self.__url

    @staticmethod
    def read_links():
        """Read links from file and remove newline characters."""
        with open('data/links.txt') as f:
            links = [link.strip('\n') for link in f]
        return links

    @staticmethod
    def csv_to_df(*args):
        """Convert csv file to Pandas DataFrame"""
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

    @staticmethod
    def price_scraping(links):
        """Extract specific statistics data from websites,
            parse and write to csv file
        """
        for link in links:

            # fixing mod_security problem
            # https://stackoverflow.com/questions/16627227/http-error-403-in-python-3-web-scraping
            req = Request(link, headers={'User-Agent': 'Mozilla/5.0'})

            page = urlopen(req)
            soup = BeautifulSoup(page, 'html.parser')
            str_soup = str(soup)

            pattern = re.compile(
                r'\"statistics\"\:\{\"pageInfo\"\:\{\"lowestPrice\"\:.*nodes'
                r'\"\:\[(.*)\]\}\,\"priceForecast', re.MULTILINE)
            data = re.findall(pattern, str_soup)
            pattern_name = re.compile(r'\"Product\",\"name\":\"(.*)\",\"'
                                      r'description\":\"Price history',
                                      re.MULTILINE)
            data_name = re.findall(pattern_name, str_soup)

            # remove chars
            raw_text = data[0]
            chars = ['{', '}', '"date":', '"lowestPrice":', '"']

            for c in chars:
                raw_text = raw_text.replace(c, "")
            split_text = raw_text.split(',')

            # convert list to dictionary
            list_to_dict = dict(
                itertools.zip_longest(*[iter(split_text)] * 2, fillvalue=""))

            # create dataframe from dict
            df_obj = pd.DataFrame.from_dict(list_to_dict, orient='index',
                                            columns=None)
            df_obj['premium'] = ut.deduce_premium_no(float(df_obj.iloc[3, 0]))

            # add column with name of mobile phone
            df_obj['Phone name'] = data_name[0]
            print(df_obj)

            # create file name
            dir_name = 'data'
            filename_suffix = 'csv'
            base_filename = 'out'
            no_of_file = str(
                int(ut.deduce_premium_no(float(df_obj.iloc[3, 0]))))

            path = os.path.join(dir_name,
                                no_of_file
                                + base_filename
                                + "."
                                + filename_suffix)

            # write dataframe to csv file
            pd.DataFrame(df_obj).to_csv(path, header=False,
                                        quoting=csv.QUOTE_NONE)

    def create_final_dataset(self):
        """Create final csv datafile,
            concat datasets from various premium number datasets
        """

        if self._get_data == 'website':
            df_concat = self.csv_to_df('data/2out.csv', 'data/3out.csv',
                                       'data/4out.csv', 'data/5out.csv',
                                       'data/6out.csv', 'data/7out.csv',
                                       'data/8out.csv')

            # save concat df to csv
            pd.DataFrame(df_concat).to_csv('data/out_concat.csv', header=False,
                                           quoting=csv.QUOTE_NONE)
            print('!!!!csv file from website!!!!')
            return 1

        if self._get_data == 'database':
            postgre_sql.postgre_sql_copy_table_to_csv_file()
            print('!!!!csv file from database!!!!')
            return 1

        print('error during creating out_concat_file.csv')
        return -1
