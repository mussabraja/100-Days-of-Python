import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard

title = Turtle()
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 260)
title.write("Pong Game by Mussab", align="center", font=("Arial", 18, "normal"))
screen = Screen()

screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)
screen.listen()

ball = Ball()
scorecard = Scorecard()

right_paddle = Paddle((350,0))
left_paddle = Paddle ((-350,0))

screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scorecard.update_scorecard_left()
    if ball.xcor() < -380:
        ball.reset_position()
        scorecard.update_scorecard_right()
screen.exitonclick()
