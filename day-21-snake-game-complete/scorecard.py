from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,220)
        self.update_scorecard()

    def inc_score(self):
        self.score +=1
        self.clear()
        self.update_scorecard()

    def update_scorecard(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 16, "normal"))
