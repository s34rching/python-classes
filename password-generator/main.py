import random
import characters

print("Welcome to the PyPassword Generator!")
letters_count = int(input("How many letters would you like in your password?\n> "))
symbols_count = int(input(f"How many symbols would you like?\n> "))
numbers_count = int(input(f"How many numbers would you like?\n> "))

letters = []
symbols = []
numbers = []

if letters_count > 0:
    for letter in range(1, letters_count + 1):
        random_letter = characters.letters[random.randint(0, len(characters.letters) - 1)]
        letters.append(random_letter)

if numbers_count > 0:
    for number in range(1, numbers_count + 1):
        random_number = characters.numbers[random.randint(0, len(characters.numbers) - 1)]
        numbers.append(random_number)

if symbols_count > 0:
    for symbol in range(1, symbols_count + 1):
        random_symbol = characters.symbols[random.randint(0, len(characters.symbols) - 1)]
        symbols.append(random_symbol)


password_length = len(letters) + len(symbols) + len(numbers)

non_empty_sets = []

for char_set in [letters, symbols, numbers]:
    if len(char_set) > 0:
        non_empty_sets.append(char_set)

password = ""

for _ in range(0, password_length):
    set_index = random.randint(0, len(non_empty_sets) - 1)
    target_set = non_empty_sets[set_index]

    if (len(target_set) > 0):
        set_char = ""

        if (len(target_set) > 1):
            char_index = random.randint(0, len(target_set) - 1)

            set_char = target_set[char_index]
            del target_set[char_index]
        else:
            set_char = target_set[0]
            del target_set[0]
            del non_empty_sets[set_index]

        password += set_char
    else:
        del non_empty_sets[set_index]

print(f"Your password is: {password}")

