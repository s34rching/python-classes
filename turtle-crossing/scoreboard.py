from turtle import Turtle
ALIGNMENT = "center"
FONT_CONFIG = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.collisions = 0
        self.color("black")
        self.goto(-240, 260)
        self.round = 1
        self.show()

    def show(self):
        self.write(f"Round {self.round}", align=ALIGNMENT, font=FONT_CONFIG)

    def update(self):
        self.clear()
        self.show()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over. You've been hit by car", align=ALIGNMENT, font=FONT_CONFIG)
