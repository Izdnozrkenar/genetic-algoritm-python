def goal_function(book,preferences,preferred_price):
    price = total_price(book)

    return price + price_difference(price,preferred_price) + preference_score(book,preferences)

def total_price(book):
    return cover_price(book[0]) + paper_price(book[1:3]) + font_price(book[3:5])

def cover_price(feature):
    prices = {
        "0": 2,
        "1": 4
    }
    return prices.get(feature)

def paper_price(feature):
    prices = {
        "00": 1,
        "01": 3,
        "10": 5,
        "11": 2
    }
    return prices.get(feature)

def font_price(feature):
    prices = {
        "00": 1,
        "01": 1,
        "10": 3,
        "11": 4
    }
    return prices.get(feature)

def price_difference(price, preferred_price):
    print(price,preferred_price)
    if(price == preferred_price or (abs(price - preferred_price) < 1) ):
        return 1
    else:
        return abs(1/(abs(price - preferred_price)))

def preference_score(book,preferences):
    print(book)
    return preferences["cover"][book[0]] + preferences["paper"][book[1:3]] + preferences["font"][book[3:5]]


