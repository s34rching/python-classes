from turtle import Turtle, Screen
from random import randint

move_min_distance = 1
move_max_distance = 10
initial_x = -230
initial_y = -130
start_shift_distance = 40


screen = Screen()
screen.setup(width=500, height=500)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
turtles = []

for index in range(len(colors)):
    turtle_the_racer = Turtle(shape="turtle")
    turtle_the_racer.color(colors[index])
    turtles.append(turtle_the_racer)

    start_y = initial_y + index * start_shift_distance

    turtle_the_racer.penup()
    turtle_the_racer.goto(x=initial_x, y=start_y)

user_bet = screen.textinput(title="Make your bet", prompt="Which color will win?")

is_on_track = True

while is_on_track:
    for racer in turtles:
        move_distance = randint(move_min_distance, move_max_distance)
        racer.forward(move_distance)

        if racer.xcor() > 230:
            is_on_track = False
            winner_index = turtles.index(racer)
            winner_color = colors[winner_index]

            if user_bet == winner_color:
                print("You racer has won!")

            print(f"{winner_color.capitalize()} has won, you've been too close!")


screen.exitonclick()
