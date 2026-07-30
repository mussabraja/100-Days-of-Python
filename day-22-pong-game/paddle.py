from turtle import Turtle, Screen
import random
class Paddle (Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)

    def move_paddle_down(self):
        new_down = self.ycor() - 20
        self.sety(new_down)
