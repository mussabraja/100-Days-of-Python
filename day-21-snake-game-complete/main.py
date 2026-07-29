from turtle import Turtle,Screen
import time
from food import Food
from snake import Snake
from scorecard import Scorecard

screen = Screen()
screen.setup(height=500,width=500)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Scorecard()


screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_mov()

    if snake.snake_new[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scorecard.inc_score()

    if snake.snake_new[0].xcor() > 250 or snake.snake_new[0].xcor() < -250 or snake.snake_new[0].ycor() > 250 or snake.snake_new[0].ycor() < -250:
        game_is_on = False
        scorecard.game_over()

    if snake.snake_hit_tail():
        game_is_on = False
        scorecard.game_over()
screen.exitonclick()
