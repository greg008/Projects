
# convert price to premium number depending on starting price
def deduce_premium_no(starting_price):
    if (starting_price < 300) and (starting_price) >= 200:
        return 2
    elif (starting_price < 400) and (starting_price) >= 300:
        return 3
    elif (starting_price < 500) and (starting_price) >= 400:
        return 4
    elif (starting_price < 600) and (starting_price) >= 500:
        return 5
    elif (starting_price < 700) and (starting_price) >= 600:
        return 6
    elif (starting_price < 800) and (starting_price) >= 700:
        return 7
    elif (starting_price < 900) and (starting_price) >= 800:
        return 8
    else:
        print('Begining price is not in the correct range')
