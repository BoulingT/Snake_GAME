from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.refresh()

    def refresh(self):
        new_random_x = random.randint(-280, 280)
        new_random_y = random.randint(-280, 280)
        self.goto(new_random_x, new_random_y)




