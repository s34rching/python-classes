import os
import random


MIN_NUMBER = 1
MAX_NUMBER = 100
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def set_attempts_count():
    difficulty_level_answer = input("Please choose a difficulty. Type 'easy' or 'hard': ")

    if (difficulty_level_answer == 'easy'):
        return EASY_LEVEL_ATTEMPTS
    return HARD_LEVEL_ATTEMPTS


def get_state_message(guess_attempts, user_guess, random_number):
    if (guess_attempts == 0):
        return f"You ran out of attempts. You lost... The number was {random_number}"
    elif (user_guess == random_number):
        return f"You won! The number was {random_number}"
    elif (user_guess < random_number):
        return "Too low"
    elif (user_guess > random_number):
        return "Too high"


def number_guessing_game():
    print("Welcome to the Number Guessing Game")

    is_continue_playing = True
    while is_continue_playing:
        user_guess = 0
        guess_attempts = 0

        os.system("clear")

        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)

        print("I'm thinking of a number between 1 and 100")

        guess_attempts = set_attempts_count()

        while (not random_number == user_guess) and (guess_attempts > 0):
            print(f"You have {guess_attempts} attempts to guess the number")
            user_guess_input = input("Make a guess: ")
            user_guess = int(user_guess_input)

            guess_attempts -= 1

            print(get_state_message(guess_attempts, user_guess, random_number))

        should_continue = input("Would you like to play one more time? 'yes' or 'no': ")
        if (not should_continue == 'yes'):
            is_continue_playing = False

number_guessing_game()
