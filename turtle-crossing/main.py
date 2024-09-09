from turtle import Screen
from pedestrian import Pedestrian
from car import Car
from random import randint
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)
screen.listen()
screen.colormode(255)

pedestrian = Pedestrian()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=pedestrian.move)

is_accident = False

while not is_accident:
    traffic_speed = 0.5
    is_moving = True
    scoreboard.show()

    while is_moving:
        traffic_speed *= 0.5
        iteration = 0
        scoreboard.update()
        is_crossed_highway = False
        cars = []
        pedestrian.refresh()
        screen.update()

        while not is_crossed_highway and not is_accident:
            iteration += 1

            if iteration % 3 == 0:
                new_cars_count = randint(0, 1)

                for car_number in range(new_cars_count):
                    car = Car()
                    cars.append(car)

            for individual_car in cars:
                individual_car.move()

                if individual_car.distance(pedestrian) < 27 and pedestrian.is_on_car_line(individual_car):
                    is_accident = True
                    is_moving = False
                    scoreboard.game_over()

            if pedestrian.ycor() > 240:
                is_crossed_highway = True
                scoreboard.round += 1

                for traffic_car in cars:
                    traffic_car.hideturtle()

            screen.update()
            time.sleep(traffic_speed)


screen.exitonclick()
