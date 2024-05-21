print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# ""
# "You enter a room of beasts. Game Over."
# "You chose a door that doesn't exist. Game Over."

game_over_message = "Your game is over"

crossroad_answer = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\"\n> ")

if (crossroad_answer.lower() == "left"):
    island_answer = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n> ")

    if (island_answer.lower() == "wait"):
        doors_answer = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n> ")

        if (doors_answer.lower() == "red"):
            print("It's a room full of fire.")
            print(game_over_message)
        elif (doors_answer.lower() == "blue"):
            print("You enter a room of beasts")
            print(game_over_message)
        elif (doors_answer.lower() == "yellow"):
            print("You found the treasure! You Win!")
        else:
            print("You have not chosen a door, you have stuck forever there")
    else:
        print("You've been attacked by angry trout")
        print(game_over_message)
else:
    print("You are falling into a hole.")
    print(game_over_message)