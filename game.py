from deck import Deck
from dealer import Dealer
from player import Player
from helperFunctions import *

def show_hand(cards, hide_one = False):
    if(not hide_one):
        print("\t\t\t    {} {}".format(cards[0], cards[1]))
    else:
        print("\t\t\t      {}".format(cards[1]))

def clear_screen(lines = 50):
    for line in range(lines):
        print("\n")

def draw_title():
    print("""
                    *************************
                    *                       *
                    *       BLACKJACK       *
                    *                       *
                    *************************
    """)

def draw_player_options():
    print("""
******************************************************************
*       1. Hit             2. Stay            3. Double Down     *
*       4. Split           5. Insurance                          *
******************************************************************
    """)

d = Deck()
dealer = Dealer()
player = Player()

d.build_deck()
d.shuffle_deck()
d.deal_cards([player, dealer])

player.hand_total = calculate_hand_total(player.hand)
dealer.hand_total = calculate_hand_total(dealer.hand)

clear_screen()
draw_title()
show_hand(dealer.hand, True)

clear_screen(11)

show_hand(player.hand)

draw_player_options()