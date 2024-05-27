from ascii_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def encrypt(text_input, shift_input, direction_input):
    if direction_input in ["encode", "decode"]:
        shift = shift_input % len(alphabet)

        encryption_alphabet = alphabet[shift:] + alphabet[:shift]

        initial_alphabet = []
        encoding_alphabet = []

        if direction_input == "encode":
            initial_alphabet = alphabet
            encoding_alphabet = encryption_alphabet
        elif direction_input == "decode":
            initial_alphabet = encryption_alphabet
            encoding_alphabet = alphabet

        encrypted_text = ""

        for character in text_input:
            if character in initial_alphabet:
                index = initial_alphabet.index(character)
                encrypted_text += encoding_alphabet[index]
            else:
                encrypted_text += character

        print(f"The {direction_input}d text is: {encrypted_text}")
    else:
        print("Direction is not set")

def recursive_encryption():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    encrypt(text, shift, direction)

    proceed_decision = input("Do you want to proceed ('yes' or 'no')?: ")

    if (proceed_decision == "yes"):
        recursive_encryption()
    else:
        print("Bye")

recursive_encryption()