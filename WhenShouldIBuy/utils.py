
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
