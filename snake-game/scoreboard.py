from turtle import Turtle
import os

ALIGNMENT = "center"
FONT_CONFIG = ("Courier", 15, "normal")

high_score_filename = "snake-game/high_score.txt"


def read_high_score():
    if os.path.isfile(high_score_filename):
        with open(high_score_filename, mode="r") as file:
            high_score = file.read()
            return int(high_score)
    return 0


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = read_high_score()
        self.color("white")
        self.goto(0, 280)
        self.show()

    def show(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT_CONFIG)

    def update(self):
        self.score += 1
        self.show()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.show()

    def save_high_score(self):
        with open(high_score_filename, mode="w") as file:
            file.write(str(self.high_score))
