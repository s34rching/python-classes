from turtle import Turtle
ALIGNMENT = "center"
FONT_CONFIG = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.collisions = 0
        self.color("white")
        self.goto(0, 280)
        self.show()

    def show(self):
        self.write(f"Score: {self.collisions}", align=ALIGNMENT, font=FONT_CONFIG)

    def update(self):
        self.clear()
        self.collisions += 1
        self.show()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT_CONFIG)
