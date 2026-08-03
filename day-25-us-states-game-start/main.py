from turtle import Turtle, Screen
import pandas

screen = Screen()

no_of_guesses = 0

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
tur_im = Turtle(image)
df = pandas.read_csv("50_states.csv")

while no_of_guesses < 50:
    answer_state = screen.textinput(title=f"{no_of_guesses}/50",prompt='What is the other state name?')
    if answer_state is None:
        break
    answer_state = answer_state.title()
    if df['state'].eq(answer_state).any():
        no_of_guesses += 1
        value_row = df[df.state == answer_state]
        x_value = value_row.x.values[0]
        y_value = value_row.y.values[0]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_value,y_value)
        t.write(answer_state)
screen.exitonclick()