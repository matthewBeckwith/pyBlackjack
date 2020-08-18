from deck import Deck
from dealer import Dealer
from player import Player
from helperFunctions import *

def show_hand(cards, hide_one = False):
    if(not hide_one):
        for card in cards:
            print(card)
    else:
        print(cards[1])

def clear_screen(lines = 50):
    for line in range(lines):
        print("\n")

def draw_title():
    print("\t\t\t*************************")
    print("\t\t\t*\tBLACKJACK\t*")
    print("\t\t\t*************************")

d = Deck()
dealer = Dealer()
player = Player()

d.build_deck()
print("Deck: ", d.deck)
d.shuffle_deck()
print("Shuffled: ", d.deck)

d.deal_cards([player, dealer])

player.hand_total = calculate_hand_total(player.hand)
dealer.hand_total = calculate_hand_total(dealer.hand)

clear_screen()
draw_title()
clear_screen(3)

print("Dealer: ")
show_hand(dealer.hand, True)
print("Dealer hand total: ", dealer.hand_total)

clear_screen(2)

print("Player: ")
show_hand(player.hand)
print("Player hand total: ", player.hand_total)

clear_screen(5)