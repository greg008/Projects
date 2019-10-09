# https://pricespy.co.uk/phones-gps/mobile-phones/samsung-galaxy-j1-mini-prime-sm-j106h--p4020352/statistics
# view-source:https://pricespy.co.uk/phones-gps/mobile-phones/huawei-p9-lite--p3637775/statistics
from urllib.request import urlopen
import re
import csv
from bs4 import BeautifulSoup
import itertools
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
rm_characters = data[0].replace('}', '')
rm_characters = rm_characters.replace('{', '')
rm_characters = rm_characters.replace('"date":', '')
rm_characters = rm_characters.replace('"lowestPrice":', '')
# rm_characters = data[0].strip('}')
print(type(rm_characters))
print('rm_char', rm_characters)
split_data = rm_characters.split(',')
print(len(split_data))
print('split_data', split_data)
# https://stackoverflow.com/questions/6900955/python-convert-list-to-dictionary
d = dict(itertools.zip_longest(*[iter(split_data)] * 2, fillvalue=""))
print(d)
print(type(d))
# for i in range(len(split_data)):
#     print(split_data[i])
#     print('\n')

# ['{"date":"2016-06-01","lowestPrice":264.91},{"date":"2016-06-02","lowestPrice":265.12},
# ['{"date":"2016-06-01","lowestPrice":264.91},{"date":"2016-06-02","lowestPrice":265.12},
# convert to json

# convert to dict
# y = json.loads(d)

# write to csv
csv_file = "Names.csv"
csv_columns = ['Data', 'Price']
with open(csv_file, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for data in d:
        writer.writerow(data)


