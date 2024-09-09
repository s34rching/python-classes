from turtle import Turtle

START_X = 0
START_Y = -270
DIRECTION = 90


class Pedestrian(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.refresh()

    def refresh(self):
        self.penup()
        self.setheading(DIRECTION)
        self.goto(START_X, START_Y)

    def move(self):
        self.forward(10)

    def is_on_car_line(self, car):
        return car.ycor() - 20 < self.ycor() < car.ycor() + 20
