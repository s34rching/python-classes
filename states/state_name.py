from turtle import Turtle


ALIGNMENT = "center"
FONT_CONFIG = ("Courier", 8, "normal")


class StateName(Turtle):
    def __init__(self, state_name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x, y)
        self.write(state_name, align=ALIGNMENT, font=FONT_CONFIG)
