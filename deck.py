import random

class Deck:
    def __init__(self):
        self.cards = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        self.suits = {"hearts": "\u2665", "diamonds": "\u2666", "clubs": "\u2663", "spades": "\u2660"}
        self.deck = []

    def build_deck(self):
        for suit in self.suits:
            for card in self.cards:
                self.deck.append(str(card + " " + self.suits[suit]))
            
    def shuffle_deck(self):
        self.deck = random.sample(self.deck, len(self.deck))

    def deal_cards(self, players):
        for x in range(len(players)):
            for player in players:
                player.hand.append(self.give_card())

    def give_card(self):
        return self.deck.pop(0)