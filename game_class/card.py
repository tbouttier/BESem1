from enum import IntEnum

class Color(IntEnum):
    CARREAU = 0
    PIQUE = 1
    COEUR = 2
    TREFLE = 3


class Value(IntEnum):
    SEPT = 0
    HUIT = 1
    NEUF = 2
    DIX = 3
    VALET = 4
    REINE = 5
    ROI = 6
    AS = 7
    
class Card:
    
    def __init__(self,color,value):
        self.color = Color(color)
        self.value = Value(value)
        
    def __str__(self) -> str:
        return f"{Color(self.color).name},{Value(self.value).name}"