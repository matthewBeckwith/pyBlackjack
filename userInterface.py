import curses

from game import Game

game = Game()
title = "BLACKJACK"

def container(screen):
    screen.clear()
    draw_header(screen)
    draw_game_table(screen)
    draw_player_options_menu(screen)

def draw_header(screen):
    h, w = screen.getmaxyx()
    x = w//2 - len(title)

    money = game.player.get_money()
    screen.addstr(1, 4, "Money:")
    screen.attron(curses.color_pair(2))
    screen.addstr(1, 11, "${}".format(money))
    screen.attroff(curses.color_pair(2))
    screen.addstr(1, x, title)

def draw_game_table(screen):
    draw_dealer_cards(screen)
    draw_player_cards(screen)

def draw_player_options_menu(screen):
    current_index = game.current_index
    options = game.current_options
    h, w = screen.getmaxyx()
    y = h//4 * 4

    for index, option in enumerate(options):
        x = w//len(options) * index

        if(index == current_index):
            screen.attron(curses.color_pair(1))
            screen.addstr(y, x, "   {}   ".format(option))
            screen.attroff(curses.color_pair(1))
        else:
            screen.addstr(y, x, "   {}   ".format(option))

def draw_dealer_cards(screen):
    h, w = screen.getmaxyx()
    y = h//4
    x = w//2 - len(game.dealer.get_hand()) * 4

    for index, card in enumerate(game.dealer.hand):
        screen.addstr(y, x + index * 5, card)

def draw_player_cards(screen):
    h, w = screen.getmaxyx()
    y = h//4 * 3
    x = w//2 - len(game.player.get_hand()) * 4

    for index, card in enumerate(game.player.hand):
        screen.addstr(y, x + index * 5, card)

def main(screen):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    container(screen)

    while(1):
        key = screen.getch()

        current_index = game.current_index
        current_options = game.current_options

        container(screen)

        if(key == curses.KEY_LEFT and current_index > 0):
            game.current_index -= 1
        elif(key == curses.KEY_RIGHT and current_index < len(current_options) - 1):
            game.current_index += 1
        elif(key == curses.KEY_ENTER or key in [10, 13]):
            if(current_options[current_index] == "Bet Min"):
                game.run(5)
                container(screen)
                key = screen.getch()
            elif(current_options[current_index] == "Bet Max"):
                game.run(10)
                container(screen)
                key = screen.getch()
            elif(current_options[current_index] == "Hit"):
                game.deck.give_card(game.player)
            elif(current_options[current_index] == "Exit"):
                break
            else:
                screen.clear()
                screen.addstr(0, 0, "You picked: {}".format(current_options[current_index]))
                key = screen.getch()
                screen.refresh()
                
        container(screen)
        screen.refresh()
curses.wrapper(main)