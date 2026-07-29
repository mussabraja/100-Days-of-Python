from turtle import Turtle
class Snake:
    def __init__(self):
        self.snake_new = []
        self.create_snake()

    def create_snake(self):

        position = [(0, 0), (-20, 0), (-40, 0)]

        for t in range(3):
            self.new_t = Turtle(shape='square')
            self.new_t.penup()
            self.new_t.color('white')
            self.new_t.goto(position[t])
            self.snake_new.append(self.new_t)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_new.append(new_segment)

    def snake_hit_tail(self):
        for segment in self.snake_new[1:]:
            if self.snake_new[0].distance(segment) < 10:
                return True
        return False

    def extend(self):
        self.add_segment(self.snake_new[-1].position())

    def snake_mov(self):
        for seg_num in range(len(self.snake_new) - 1, 0, -1):
            nex_x = self.snake_new[seg_num - 1].xcor()
            new_y = self.snake_new[seg_num - 1].ycor()
            self.snake_new[seg_num].goto(nex_x, new_y)
        self.snake_new[0].forward(20)

    def up(self):
        if self.snake_new[0].heading() != 270:
            self.snake_new[0].setheading(90)

    def down(self):
        if self.snake_new[0].heading() != 90:
            self.snake_new[0].setheading(270)

    def left(self):
        if self.snake_new[0].heading() != 0:
            self.snake_new[0].setheading(180)

    def right(self):
        if self.snake_new[0].heading() != 180:
            self.snake_new[0].setheading(0)
