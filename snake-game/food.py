from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.x = 0
        self.y = 0
        self.refresh(screen_width, screen_height)

    def refresh(self, screen_width, screen_height):
        snake_size = 20

        self.x = randint(-int(screen_width / 2 - snake_size), int(screen_width / 2 - snake_size))
        self.y = randint(-int(screen_height / 2 - snake_size), int(screen_height / 2 - snake_size))
        self.goto(self.x, self.y)