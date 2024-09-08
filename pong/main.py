from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

ball = Ball()
left_paddle = Paddle("left", SCREEN_WIDTH)
right_paddle = Paddle("right", SCREEN_WIDTH)
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
screen.onkey(key="w", fun=left_paddle.up)
screen.onkey(key="s", fun=left_paddle.down)

is_game_on = True
max_score = 10
last_scorer = ''

while scoreboard.left_score < max_score and scoreboard.right_score < max_score:
    scoreboard.show()
    ball.refresh(last_scorer)
    screen.update()
    is_ball_moving = True

    while is_ball_moving:
        ball.move(left_paddle, right_paddle)
        screen.update()
        time.sleep(ball.move_speed)

        if ball.xcor() > 350:
            is_ball_moving = False
            scoreboard.left_score += 1
            last_scorer = 'left'
        if ball.xcor() < -350:
            is_ball_moving = False
            scoreboard.right_score += 1
            last_scorer = 'right'

        scoreboard.update()

    if scoreboard.left_score == max_score:
        ball.clear()
        scoreboard.game_over('Left')
    elif scoreboard.right_score == max_score:
        ball.clear()
        scoreboard.game_over('Right')

screen.exitonclick()
