"""
Helpers for web_price_scraping module
"""


def deduce_premium_no(starting_price):
    """Convert price to premium number depending on starting price"""
    premium_no = 0
    if 300 > starting_price >= 200:
        premium_no = 2
    elif 400 > starting_price >= 300:
        premium_no = 3
    elif 500 > starting_price >= 400:
        premium_no = 4
    elif 600 > starting_price >= 500:
        premium_no = 5
    elif 700 > starting_price >= 600:
        premium_no = 6
    elif 800 > starting_price >= 700:
        premium_no = 7
    elif 900 > starting_price >= 800:
        premium_no = 8

    if premium_no != 0:
        return premium_no

    raise TypeError('wrong range')
