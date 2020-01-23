from enum import Enum

class Book():
    def __init__(self,binary):
        self.binary = list(binary)

    def update_binary(self,list_to_update):
        self.binary = ''.join(list_to_update)

#prices for book features
class Covers(Enum):
    soft = 0
    hard = 1

class Papers(Enum):
    polished_chalk = 0
    dull_chalk = 1
    decorative = 2
    thin = 3

class Fonts(Enum):  
    serif = 0
    sanf_serif = 1
    decorative = 2
    mono_spaced = 3


