import random
import images

user_input = input("What do you choose? Rock, Paper or Scissors?\n> ")

choice_map = ["rock", "paper", "scissors"]
images_map = [images.rock, images.paper, images.scissors]

result = ""

if (user_input.lower() in choice_map):
    user_index = choice_map.index(user_input.lower())
    computer_index = random.randint(0, len(choice_map) - 1)

    result = ""

    if ((user_index == 0 and computer_index == 2) or (user_index == 1 and computer_index == 0) or (user_index == 2 and computer_index == 1)):
        result = "You've won!"
    elif (user_index == computer_index):
        result = "Fair draw!"
    else:
        result = "You've lost..."

    print(images_map[user_index])
    print(f"Computer choice is: {choice_map[computer_index].capitalize()}")
    print(images_map[computer_index])
else:
    result = "Please pick 1 out of 3 allowed options (Rock, Paper or Scissors)"

print(result)

