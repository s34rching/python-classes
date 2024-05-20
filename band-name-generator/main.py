#1. Create a greeting for your program.
#2. Ask the user for the city that they grew up in.
#3. Ask the user for the name of a pet.
#4. Combine the name of their city and pet and show them their band name.
#5. Make sure the input cursor shows on a new line

print("Hey! This is free band name generator!")

user_city = input("What is your city? ")
user_pet = input("What is your pet name? ")

band_name = f"{user_city.capitalize()} {user_pet.capitalize()}"

print(f"Suggested band name is: {band_name}")