from turtle import Turtle, Screen
import random
import turtle

turtle.colormode(255)
timmy_the_turtle = Turtle()
color_list = [(226, 225, 222), (197, 170, 7), (31, 101, 182), (215, 65, 99), (32, 19, 15), (158, 3, 41), (223, 142, 43), (110, 161, 203), (221, 59, 24), (0, 55, 141), (61, 41, 60), (0, 118, 83), (199, 50, 121), (203, 212, 219), (16, 125, 91), (203, 137, 158), (222, 202, 118), (220, 204, 209), (34, 153, 192), (217, 224, 221), (215, 83, 57), (108, 112, 173), (216, 177, 187), (135, 175, 157), (220, 177, 171), (86, 151, 129), (182, 189, 207), (237, 198, 2), (81, 57, 49), (176, 201, 191)]

for n in range (10):
    for i in range(10):
        timmy_the_turtle.dot(20,random.choice(color_list))
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
        timmy_the_turtle.pendown()
    timmy_the_turtle.setheading(90) #uper
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(180) #left
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(500)
    timmy_the_turtle.setheading(0)


screen = Screen()
screen.exitonclick()
