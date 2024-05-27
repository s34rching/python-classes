import os
import random
from stages_graphics import stages, logo
from words import word_list

print(logo)

chosen_word = random.choice(word_list)

word_pattern = ["_"] * len(chosen_word)
displayed = " ".join(word_pattern)
word_letters = list(chosen_word)

lives_count = len(stages) - 1
is_user_won = False

while lives_count > 0 and not is_user_won:
    print(stages[lives_count])
    displayed = " ".join(word_pattern)
    print(f"{displayed}\n")

    user_guess = input("Could you guess a letter?\n> ")
    os.system('clear')
    user_letter = user_guess.lower()

    if user_letter in word_pattern:
        print(f"You\'ve already guessed '{user_letter}', make another choice")
    else:
        if user_letter in word_letters:
            for letter_index in range(0, len(word_letters)):
                if user_letter == word_letters[letter_index]:
                    word_pattern[letter_index] = user_letter
                    guessed = "".join(word_pattern)

                    if guessed == chosen_word:
                        print("Congratulations! You're still alive!")
                        is_user_won = True
        else:
            lives_count -= 1
            print(f"Ahh, nah, '{user_letter}' is not in here. Minus a life. You have {lives_count} lives")

            if not lives_count:
                print("Unfortunately! You're taking that place!")

