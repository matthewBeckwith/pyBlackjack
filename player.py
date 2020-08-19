from helperFunctions import *

class Player:
    def __init__(self):
        self.hand = []
        self.hand_total = 0
        self.money = 1000
    
    def get_money(self):
        return self.money

    def add_money(self, amount):
        self.money += amount

    def subtract_money(self, amount):
        self.money -= amount

    def get_hand_value(self):
        return self.hand_total

    def set_hand_value(self):
        self.hand_total = calculate_hand_total(self.hand)

    def get_hand(self):
        return self.hand

    def put_card_in_hand(self, card):
        self.hand.append(card)