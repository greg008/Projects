# https://pricespy.co.uk/phones-gps/mobile-phones/samsung-galaxy-j1-mini-prime-sm-j106h--p4020352/statistics
# view-source:https://pricespy.co.uk/phones-gps/mobile-phones/huawei-p9-lite--p3637775/statistics
from urllib.request import urlopen
import re
import csv
from bs4 import BeautifulSoup
import itertools

import pandas as pd

def priceScraping():
    quote_page = 'https://pricespy.co.uk/phones-gps/mobile-phones/huawei-p9-lite--p3637775/statistics'
    # quote_page = 'https://pricespy.co.uk/phones-gps/mobile-phones/samsung-galaxy-s9-sm-g960f-64gb--p4700492/statistics'
    page = urlopen(quote_page)
    soup = BeautifulSoup(page, 'html.parser')
    soup2 = str(soup)
    # print(soup2)
    # write data.txt
    # html = soup.prettify("utf-8")
    # with open("data.txt", "w") as file:
    #     file.write(str(html))

    pattern = re.compile('\"statistics\"\:\{\"pageInfo\"\:\{\"lowestPrice\"\:.*nodes\"\:\[(.*)\]\}\,\"priceForecast', re.MULTILINE)
    data = re.findall(pattern, soup2)

    pattern_name = re.compile('\"Product\",\"name\":\"(.*)\",\"description\":\"Price history', re.MULTILINE)
    data_name = re.findall(pattern_name, soup2)
    print('data_name xxxxxxxxxxxxxxx', data_name)
    print('data name[0] = ', data_name[0])

    # print(type(data))
    # data = dict(data)
    print(data)
    rm_characters = data[0].replace('}', '')
    rm_characters = rm_characters.replace('{', '')
    rm_characters = rm_characters.replace('"date":', '')
    rm_characters = rm_characters.replace('"lowestPrice":', '')
    rm_characters = rm_characters.replace('"', '')
    # rm_characters = data[0].strip('}')
    print(type(rm_characters))
    print('rm_char', rm_characters)
    split_data = rm_characters.split(',')
    print(len(split_data))
    print('split_data', split_data)
    # https://stackoverflow.com/questions/6900955/python-convert-list-to-dictionary
    d = dict(itertools.zip_longest(*[iter(split_data)] * 2, fillvalue=""))
    print('d', d)
    print(type(d))

    dfObj = pd.DataFrame.from_dict(d, orient='index', columns=None)
    # print('dfObj', dfObj)
    # print('dfObj type', type(dfObj))
    # add class type [premium, mid-range]
    if float(dfObj.iloc[0, 0]) > 600:
        dfObj['premium'] = 1
    else:
        dfObj['premium'] = 0
    # add name of mobile phone
    dfObj['Phone name'] = data_name[0]

    # print('iloc 0 0 ', dfObj.iloc[0, 0])
    # print('iloc 0 0  type', type(dfObj.iloc[0, 0]))
    # dfObj['premium'] = 1
    print('dfObj_after', dfObj)
    # data frame to csv
    index1 = ['date', 'price']
    pd.DataFrame(dfObj).to_csv('out1.csv', header=False, quoting=csv.QUOTE_NONE)
    print('function finished')
priceScraping()