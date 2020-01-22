from book import Book, Covers, Papers, Fonts
from goal_function_helpers import goal_function

b1 = Book(11011)

pr = {
    "cover":{
        "0": 1,
        "1": 1
    },
    "paper": {
        "00": 1,
        "01": 1,
        "10": 1,
        "11": 1
    },
    "font": {
        "00": 1,
        "01": 1,
        "10": 1,
        "11": 5 
    }
}


