import random
import characters


def generate_password(letters_length, symbols_length, numbers_length):
    letters = []
    numbers = []
    symbols = []

    if letters_length > 0:
        letters = [random.choice(characters.letters) for _ in range(0, letters_length)]

    if numbers_length > 0:
        numbers = [random.choice(characters.numbers) for _ in range(0, numbers_length)]

    if symbols_length > 0:
        symbols = [random.choice(characters.symbols) for _ in range(0, symbols_length)]

    password_length = len(letters) + len(symbols) + len(numbers)

    non_empty_sets = []

    for char_set in [letters, symbols, numbers]:
        if len(char_set) > 0:
            non_empty_sets.append(char_set)

    password = ""

    for _ in range(0, password_length):
        set_index = random.randint(0, len(non_empty_sets) - 1)
        target_set = non_empty_sets[set_index]

        if len(target_set) > 0:
            set_char = ""

            if len(target_set) > 1:
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

    return password
