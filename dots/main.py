import turtle
from turtle import Turtle, Screen
from random import choice

colors_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

turtle.colormode(255)

turtle_the_drawer = Turtle()
turtle_the_drawer.speed(5)

screen = Screen()
screen.screensize(500, 500)

dots_per_size = 25
distance = 20
initial_x = -200.0
initial_y = -200.0

turtle_the_drawer.penup()
turtle_the_drawer.setposition(initial_x, initial_y)

for row in range(dots_per_size):
    coordinates = [initial_x, initial_y + distance * row]

    for column in range(dots_per_size):
        target_color = choice(colors_list)

        coordinates = [initial_x + distance * column, coordinates[1]]
        turtle_the_drawer.setposition(coordinates[0], coordinates[1])

        turtle_the_drawer.pendown()
        turtle_the_drawer.color(target_color)
        turtle_the_drawer.pencolor(target_color)
        turtle_the_drawer.dot(target_color)
        turtle_the_drawer.penup()

turtle_the_drawer.hideturtle()

screen.exitonclick()
