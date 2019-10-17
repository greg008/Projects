# add libs
import sys
# sys.path.append("..")
# import WebPriceScraping
import csv
import pandas
import numpy as np


# read data for H p9 Lite
cols = ['date', 'price', 'premium', 'name']
df1 = pandas.read_csv('out1.csv', sep=',', names=cols, header=None)
print('head:', df1.head())
print('len:', len(df1))
print('rozmiar', df1.shape)
print('\n')
# convert data to integer(number of days from begining)
df1.insert(0, 'Day', range(0, len(df1)))
print('head:', df1.tail())

# read data for Samsung Galaxy S9
cols = ['date', 'price', 'premium', 'name']
df2 = pandas.read_csv('out2.csv', sep=',', names=cols, header=None)
print('head:', df2.head())
print('len:', len(df2))
print('rozmiar', df2.shape)
print('\n')
# convert data to integer(number of days from begining)
df2.insert(0, 'Day', range(0, len(df2)))
print('head:', df2.tail())

# concenate two dataframes
df3 = pandas.concat([df1, df2], ignore_index=True)
print(df3.head())
print(df3.tail())


# save concat df to csv
pandas.DataFrame(df3).to_csv('out_concat.csv', header=False, quoting=csv.QUOTE_NONE)
print('function finished')


