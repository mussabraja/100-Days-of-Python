from turtle import Turtle
class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_scorecard()

    def update_scorecard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 16, "normal"))
        self.goto(100, 200)
        self.write(f"{self.r_score}", align="center", font=("Arial", 16, "normal"))

    def update_scorecard_left(self):
        self.l_score += 1
        self.update_scorecard()

    def update_scorecard_right(self):
        self.r_score += 1
        self.update_scorecard()
