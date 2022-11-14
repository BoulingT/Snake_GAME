from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        self.snake_body.append(new_segment)

    def extend(self):
        #add a segment to the snake
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for body_num in range(len(self.snake_body) - 1, 0, -1):
            self.new_x = self.snake_body[body_num - 1].xcor()
            self.new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(self.new_x, self.new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


