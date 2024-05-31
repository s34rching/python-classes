import os
import random
from logo import logo

ace = "A"
deck = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
cards = deck * 4
initial_cards_count = 2


def clear_screen():
    os.system("clear")


def set_player_cards(cards, count):
    random_cards = []

    for _ in range(count):
        random_card = random.choice(cards)
        random_card_index = cards.index(random_card)
        random_cards.append(random_card)
        cards.pop(random_card_index)

    return random_cards


def draw_cards(cards_set, state):
    def get_card_image(card):
        return f"[{card}]"

    cards = cards_set.copy()
    drawn_cards = f"{get_card_image(cards[0])}"
    hidden_card = "[?]"

    for card_index in range(1, len(cards)):
        if (state == "hidden"):
            drawn_cards += f" {hidden_card}"
        elif (state == 'unveiled'):
            drawn_cards += f" {get_card_image(cards[card_index])}"

    return drawn_cards


def calculate_hand_without_aces(cards_without_aces):
        hand_total = 0

        for card in cards_without_aces:
            if (card in ['J', 'Q', 'K']):
                hand_total += 10
            else:
                hand_total += card

        return hand_total


def calculate_hand(hand_cards):
    total = 0

    if ace not in hand_cards:
        total = calculate_hand_without_aces(hand_cards)
    else:
        other_cards = []

        for card in hand_cards:
            if (not str(card) == ace):
                other_cards.append(card)

        if (len(other_cards) > 0):
            total = calculate_hand_without_aces(other_cards)

        aces_count = hand_cards.count(ace)

        if (aces_count == 1 and total < 11):
            total += 11
        elif (aces_count == 2 and total < 10):
            total += 12
        elif (aces_count == 3 and total < 9):
            total += 13
        elif (aces_count == 4 and total < 8):
            total += 14
        elif (aces_count == 5 and total < 7):
            total += 15
        elif (aces_count == 6 and total < 6):
            total += 16
        elif (aces_count == 7 and total < 5):
            total += 17
        elif (aces_count == 8 and total < 4):
            total += 18
        elif (aces_count == 9 and total < 3):
            total += 19
        elif (aces_count == 10 and total < 2):
            total += 20
        elif (aces_count == 11 and total < 1):
            total += 21
        else:
            total += aces_count * 1

    return total


def get_result(player_cards, computer_cards):
    result = ""

    player_total = calculate_hand(player_cards)
    computer_total = calculate_hand(computer_cards)

    if (player_total == computer_total):
        result = "It is a draw"
    elif (player_total > 21):
        result = "You went over. You lost"
    elif (computer_total > 21 and player_total < 22):
        result = "Computer went over. You won"
    elif (player_total > computer_total):
        result = "You won"
    else:
        result = "You lost"

    print(f"Round is over")
    print(f"Computer cards: {draw_cards(computer_cards, "unveiled")} with total of {computer_total}")
    print(f"Your cards:     {draw_cards(player_cards, "unveiled")} with total of {player_total}\n")
    print(result)


def is_stop_game(player_hand, computer_hand):
    return calculate_hand(player_hand) > 21 or calculate_hand(player_hand) == 21 or calculate_hand(computer_hand) == 21


def blackjack():
    is_proceed_game = True
    while is_proceed_game:
        play_cards = cards.copy()
        want_play_input = input("Do you want to a game of Blackjack? Type 'y' or 'n': ")

        if (want_play_input == 'y'):
            clear_screen()
            print(logo)

            computer_hand = set_player_cards(play_cards, initial_cards_count)
            player_hand = set_player_cards(play_cards, initial_cards_count)

            is_get_another_card = True
            while is_get_another_card:
                print(f"Computer cards: {draw_cards(computer_hand, 'hidden')}")
                print(f"Your cards:     {draw_cards(player_hand, 'unveiled')}\n")

                if (is_stop_game(player_hand, computer_hand)):
                    is_get_another_card = False
                    get_result(player_hand, computer_hand)
                else:
                    get_another_card_input = input("Type 'y' to get another card or type 'n' to pass: ")

                    if (get_another_card_input == 'y'):
                        player_another_card = set_player_cards(play_cards, 1)
                        player_hand += player_another_card
                        print(f"\nYou've got {draw_cards(player_another_card, 'unveiled')}\n")
                    else:
                        is_get_another_card = False
                        while calculate_hand(computer_hand) < 17:
                            print(f"Computer has less than 17 and taking another_card")
                            computer_another_card = set_player_cards(play_cards, 1)
                            computer_hand += computer_another_card
                            print(f"\nComputer has got {draw_cards(computer_another_card, 'unveiled')}\n")
                            computer_total = calculate_hand(computer_hand)

                        get_result(player_hand, computer_hand)
        else:
            is_proceed_game = False


blackjack()
