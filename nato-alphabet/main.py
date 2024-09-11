import pandas

data = pandas.read_csv("./nato-alphabet/data/nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter:row.code for (_, row) in data.iterrows()}


def get_phonetic_match(letter):
    return phonetic_alphabet[str.upper(letter)]


user_word = input("Word to interpret: ")
phonetic_interpretation = [get_phonetic_match(letter) for letter in user_word]

print(data)
print(user_word)
print(phonetic_interpretation)
