
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
cards = [11, 2, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(any_list):
    score = 0
    for k in any_list:
        score += k
    return score


def print_current_score(user_cards_list, com_cards_list):
    print(f"\tYours cards: {user_cards_list}, current score: {calculate_score(user_cards_list)}")
    print(f"\tComputer's first card: {com_cards_list[0]}")


def print_score(user_cards_list, com_cards_list):  # prints the final score that at last it is called
    print(f"\tYours final hand: {user_cards_list}, final score: {calculate_score(user_cards_list)}")
    print(f"\tComputer's final hand: {com_cards_list}, final score: {calculate_score(com_cards_list)}")


def select_card(any_cards_list):
    any_cards_list.append(random.choice(cards))
    score = calculate_score(any_cards_list)
    if score == 21:
        return 2
    elif score > 21:
        return 0
    else:
        return 1


def blackjack_helper(user_cards_list, com_cards_list):
    card_next = input("Type 'y' to get another card, type 'n to pass: ")
    while card_next == 'y':
        indicator = select_card(user_cards_list)  # returns 1 if <21, 0 if > 21, and 2 if ==21
        if indicator == 2:
            print_score(user_cards_list, com_cards_list)
            print("user won by a black_jack!!!")
            play()
            return
        elif indicator == 0:
            print_score(user_cards_list, com_cards_list)
            print("Computer wins!!! because you went over ")
            play()
            return
        else:
            print("enters into the else block ")
            print_current_score(user_cards_list, com_cards_list)
            card_next = input("Type 'y' to get another card, type 'n to pass: ")

    if card_next == 'n':
        com_score = calculate_score(com_cards_list)
        while com_score < 17:
            indicator = select_card(com_cards_list)
            if indicator == 2:
                print_score(user_cards_list, com_cards_list)
                print("computer wins by blackjack")
                play()
                return
            elif indicator == 0:
                print_score(user_cards_list, com_cards_list)
                print("user won since computer went over")
                play()
                return
            else:
                com_score = calculate_score(com_cards_list)

    user_score = calculate_score(user_cards_list)
    com_score = calculate_score(com_cards_list)

    print_score(user_cards_list, com_cards_list)

    if user_score > com_score:
        print("user wins since his score is greater than computer")
    elif user_score == com_score:
        print("draw since both have an equal score")
    else:
        print("computer wins since it's score is greater!!!")

    play()


def blackjack():
    user_cards_list = [random.choice(cards), random.choice(cards)]
    com_cards_list = [random.choice(cards)]
    user_score = calculate_score(user_cards_list)

    print_current_score(user_cards_list, com_cards_list)

    if user_score == 21:
        print_score(user_cards_list, com_cards_list)
        print("user won by a black_jack!!!")
        play()
        return

    blackjack_helper(user_cards_list, com_cards_list)


def play():
    want_to_play = input("Do you want to play the game of blackjack? Type 'y' or 'n': ")
    if want_to_play == 'y':
        blackjack()
    else:
        return


play()



