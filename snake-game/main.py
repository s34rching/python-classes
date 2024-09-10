from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen_width = 600
screen_height = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

screen.listen()

snake = Snake()
food = Food(screen_width, screen_height)
scoreboard = Scoreboard()

screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.update()
        snake.append_segment()
        food.refresh(screen_width, screen_height)

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
