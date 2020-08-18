def check_int(num):
    try:
        int(num)
    except:
        return False
    return True

def remove_symbol(card):
    split_card = card.split()
    return split_card[0]

def get_card_value(card):
    card_no_symbol = remove_symbol(card)
    if(check_int(card_no_symbol)):
        return int(card_no_symbol)
    else:
        if(card_no_symbol == 'A'):
            return 11
        else:
            return 10

def calculate_hand_total(hand):
    total = 0
    for card in hand:
        card_value = get_card_value(card)
        if(card_value == 11 and total + 11 > 21):
            total += 1
        else:
            total += card_value
    return total