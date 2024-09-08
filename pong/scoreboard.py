from turtle import Turtle
ALIGNMENT = "center"
FONT_CONFIG = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.collisions = 0
        self.color("white")
        self.goto(0, 260)
        self.left_score = 0
        self.right_score = 0
        self.show()

    def show(self):
        self.write(f"{self.left_score} : {self.right_score}", align=ALIGNMENT, font=FONT_CONFIG)

    def update(self):
        self.clear()
        self.show()

    def game_over(self, side):
        self.goto(0, 0)
        self.write(f"{side} paddle has won!", align=ALIGNMENT, font=FONT_CONFIG)
