from turtle import Turtle, Screen
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.goto(random.randint(-230, 230), random.randint(-230, 230))
    def refresh(self):
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 230)
        self.goto(random_x, random_y)
