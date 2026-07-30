from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_move = self.xcor() + self.x_move
        y_move = self.ycor() + self.y_move
        self.goto(x_move,y_move)

    def bounce_y(self):
        self.y_move = -self.y_move

    def bounce_x(self):
        self.x_move = -self.x_move

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
