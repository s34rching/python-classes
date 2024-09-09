from turtle import Turtle
from generate_color import generate_color
from random import randint

DIRECTION = 180
MIN_SPAWN_X = 301
MAX_SPAWN_X = 330
MIN_SPAWN_Y = -240
MAX_SPAWN_Y = 240


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed = 5
        self.spawn()
        self.move()

    def move(self):
        self.forward(self.speed)

    def spawn(self):
        spawn_x = randint(MIN_SPAWN_X, MAX_SPAWN_X)
        spawn_y = randint(MIN_SPAWN_Y, MAX_SPAWN_Y)

        self.setheading(180)
        self.color(generate_color())
        self.goto(spawn_x, spawn_y)
