from helperFunctions import *

class Dealer:
    def __init__(self):
        self.hand = []
        self.hand_total = 0

    def get_hand(self):
        return self.hand

    def get_hand_value(self):
        return self.hand_total

    def set_hand_value(self):
        self.hand_total = calculate_hand_total(self.hand)

    def put_card_in_hand(self, card):
        self.hand.append(card)

    def showcard_is_ace(self):
        if(get_card_value(self.hand[1]) == 11):
            return True