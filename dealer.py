from helperFunctions import *

class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_total = 0

    def showcard_is_ace(self):
        if(get_card_value(self.hand[1]) == 11):
            return True