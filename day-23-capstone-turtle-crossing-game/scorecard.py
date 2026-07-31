from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-260,260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"LEVEL  {self.level}", align='left', font=('Arial', 8, 'normal'))

    def inc_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align='center', font=('Arial', 8, 'normal'))
