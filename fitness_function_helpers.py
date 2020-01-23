def fitness_function(book,group_data):
    price = total_price(book)

    return price + price_difference(price,group_data.preferred_price) + preference_score(book,group_data.preference_dictonary)

def total_price(book):
    return cover_price(book[0]) + paper_price(book[1:3]) + font_price(book[3:5])

def cover_price(feature):
    prices = {
        "0": 2,
        "1": 4
    }
    return prices.get(feature)

def paper_price(feature):
    key = "".join(feature)
    prices = {
        "00": 1,
        "01": 3,
        "10": 5,
        "11": 2
    }
    return prices.get(key)

def font_price(feature):
    key = "".join(feature)
    prices = {
        "00": 1,
        "01": 1,
        "10": 3,
        "11": 4
    }
    return prices.get(key)

def price_difference(price, preferred_price):    

    #escape edge cases => max value get here is 10
    if(price == preferred_price or (abs(price - preferred_price) < 1) ):
        return 10
    else:
        return 10*abs(1/(abs(price - preferred_price)))

def preference_score(book,preferences):
    book = "".join(book)
    return (preferences["cover"][book[0]] + preferences["paper"][book[1:3]] + preferences["font"][book[3:5]])/10


