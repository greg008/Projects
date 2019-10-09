# https://pricespy.co.uk/phones-gps/mobile-phones/samsung-galaxy-j1-mini-prime-sm-j106h--p4020352/statistics
# view-source:https://pricespy.co.uk/phones-gps/mobile-phones/huawei-p9-lite--p3637775/statistics
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
import json
import pandas as pd

quote_page = 'https://pricespy.co.uk/phones-gps/mobile-phones/huawei-p9-lite--p3637775/statistics'
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
soup2 = str(soup)

pattern = re.compile('\"statistics\"\:\{\"pageInfo\"\:\{\"lowestPrice\"\:.*nodes\"\:\[(.*)\]\}\,\"priceForecast', re.MULTILINE)
data = re.findall(pattern, soup2)
# print(type(data))
# data = dict(data)
print(data)
split_data = data[0].split(',')
print(len(split_data))
print(split_data)

for i in range(len(split_data)):
    print(split_data[i])
    print('\n')

# ['{"date":"2016-06-01","lowestPrice":264.91},{"date":"2016-06-02","lowestPrice":265.12},
# ['{"date":"2016-06-01","lowestPrice":264.91},{"date":"2016-06-02","lowestPrice":265.12},
# convert to json

# convert to dict
# y = json.loads(data)
