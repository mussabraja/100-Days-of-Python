import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(height=400,width=500)
user_bet = screen.textinput(title='Make your bet',prompt='Which turtle color will win =  ')
colors = ["red","orange","yellow","green","blue","purple"]
is_race_on = False

turtles = []

for t in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[t])
    turtles.append(new_turtle)
    new_turtle.goto(x=-230,y=t*30)


if user_bet:
    is_race_on = True

while is_race_on:
    for n in turtles:
        if n.xcor() > 230:
            is_race_on = False
            winning_color = n.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        n.forward(rand_distance)



screen.exitonclick()
