from turtle import Turtle

UP = 90
DOWN = 270
STEP_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, position, screen_width):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.locate(screen_width, position)

    def locate(self, screen_width, position):
        y_cor = 0
        side_margin = 50

        x_cor = 0

        if position == "left":
            x_cor = -screen_width / 2 + side_margin
        elif position == "right":
            x_cor = screen_width / 2 - side_margin

        self.setheading(UP)
        self.goto(x_cor, y_cor)

    def up(self):
        if self.ycor() < 250:
            self.setheading(UP)
            self.forward(STEP_DISTANCE)

    def down(self):
        if self.ycor() > -250:
            self.setheading(DOWN)
            self.forward(STEP_DISTANCE)
