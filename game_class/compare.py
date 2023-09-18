from game_class.card import Color,Value,Card

normal_order = [ Value.SEPT,
                Value.HUIT,
                Value.NEUF,
                Value.VALET,
                Value.REINE,
                Value.ROI,
                Value.DIX,
                Value.AS,
    ]

atout_order = [ Value.SEPT,
                Value.HUIT,
                Value.REINE,
                Value.ROI,
                Value.DIX,
                Value.AS,
                Value.NEUF,
                Value.VALET,
    ]

class ComparableValue:
    
    def __init__(self, value, atout=False):
        self.value = value
        
        if atout:
            self.order = atout_order
        else:
            self.order = normal_order
            
        self.ind1 = self.order.index(self.value)
        
    def __sup__(self, other):
        ind2 = self.order.index(other)
        return self.ind1>ind2
    
    def __supeg__(self, other):
        ind2 = self.order.index(other)
        return self.ind1>=ind2
    
    def __inf__(self, other):
        ind2 = self.order.index(other)
        return self.ind1<ind2
    
    def __infeg__(self, other):
        ind2 = self.order.index(other)
        return self.ind1<=ind2
    
    def __eg__(self, other):
        ind2 = self.order.index(other)
        return self.ind1==ind2

    def __supeg__(self, other):
        return not(self.__eg__(other))
    
class ComparableCard:
    
    def __init__(self,card,atout=False) -> None:
        if not(isinstance(card,Card)):
            raise TypeError(f"card doit être un objet Card, pas un {type(card)}")
        
        self.card = card
        self.atout = atout
        
    def __sup__(self, other):
        return ComparableValue(self.card.value,atout=self.atout)>ComparableValue(other.card.value,atout=self.atout)

    def __supeg__(self, other):
        return ComparableValue(self.card.value,atout=self.atout)>=ComparableValue(other.card.value,atout=self.atout)

    def __inf__(self, other):
        return ComparableValue(self.card.value,atout=self.atout)<ComparableValue(other.card.value,atout=self.atout)

    def __infeg__(self, other):
        return ComparableValue(self.card.value,atout=self.atout)>=ComparableValue(other.card.value,atout=self.atout)

    def __eg__(self, other):
        return ComparableValue(self.card.value,atout=self.atout)==ComparableValue(other.card.value,atout=self.atout)

    def __ne__(self, other):
        return not(self.__eq__(other))
