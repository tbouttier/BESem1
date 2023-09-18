from game_class.card import Color,Card,Value
from game_class.compare import ComparableCard

import copy

class Hand:
    def __init__(self,hand) -> None:
        
        for card in hand:
            if not(isinstance(card,Card)):
                raise TypeError(f"card doit être un objet Card pas un {type(card)}")
            
        self.set = copy.deepcopy(hand)
        
    def __getitem__(self,key):
        return self.set[key]
    
    def __len__(self):
        return len(self.set)
    
    def remove(self,card):
        return self.set.remove(card)
    
    def _order_little_hand(self, little_hand,atout_color):
        if len(little_hand) == 0:
            return little_hand
        
        atout = (little_hand[0].color == atout_color)
        comparable_little_hand