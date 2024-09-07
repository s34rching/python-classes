from turtle import Turtle

initial_length = 3
segment_size = 20
initial_y_coordinate = 0
turn_angle = 90
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.length = initial_length
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        for segment in range(initial_length):
            initial_x_coordinate = 0 - segment * segment_size

            snake_segment = Turtle()
            snake_segment.shape("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(initial_x_coordinate, initial_y_coordinate)
            self.segments.append(snake_segment)
            self.head = self.segments[0]

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()

            self.segments[segment_number].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)
