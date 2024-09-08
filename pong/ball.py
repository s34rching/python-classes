import random
from turtle import Turtle
from random import randint

STARTING_SPEED = 0.15


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.current_angle = 45
        self.move_speed = STARTING_SPEED

    def move(self, left_paddle, right_paddle):
        if self.ycor() > 280 or self.ycor() < -280:
            self.current_angle = self.heading()
            self.current_angle = 360 - self.current_angle

        if (self.xcor() < -330 and self.distance(left_paddle) < 40) or (self.xcor() > 330 and self.distance(right_paddle) < 40):
            self.current_angle = self.heading()
            self.current_angle = 180 - self.current_angle
            self.move_speed *= 0.9

        self.setheading(self.current_angle)
        self.forward(20)

    def refresh(self, last_scorer=''):
        self.goto(0, 0)
        self.move_speed = STARTING_SPEED

        to_right_top = randint(10, 60)
        to_right_bottom = randint(300, 350)
        to_left_top = randint(120, 170)
        to_left_bottom = randint(190, 247)

        if last_scorer == '':
            to_right = random.choice([to_right_top, to_right_bottom])
            to_left = random.choice([to_left_top, to_left_bottom])

            self.current_angle = random.choice([to_right, to_left])
        elif last_scorer == 'left':
            self.current_angle = random.choice([to_left_top, to_left_bottom])
        else:
            self.current_angle = random.choice([to_right_top, to_right_bottom])
