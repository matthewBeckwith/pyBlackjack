from deck import Deck
from dealer import Dealer
from player import Player
from helperFunctions import *

deck = Deck()
player = Player()
dealer = Dealer()

table_options = ["Bet Min", "Bet Max", "Exit"]
in_game_options = ["Hit", "Stay", "Double Down"]
alt_options = ["Split", "Insurance"]

class Game:
    def __init__(self):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.current_index = 0
        self.current_options = table_options

    def run(self, amount):
        self.deck.build_deck()
        self.deck.shuffle_deck()

        self.player.subtract_money(amount)
        self.current_options = in_game_options
        self.current_index = 0

        self.deck.deal_cards([self.player, self.dealer])

        self.player.set_hand_value()
        self.dealer.set_hand_value()

        if(cards_match(self.player.get_hand())):
            self.current_options.append(alt_options[0])
        if(self.dealer.showcard_is_ace()):
            self.current_options.append(alt_options[1])