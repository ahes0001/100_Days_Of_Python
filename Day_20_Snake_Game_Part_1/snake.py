from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
TURN_90 = 90


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # 3 20x20 turtle squares

    def create_snake(self):
        for i in range(3):
            turtle = Turtle(shape="square")
            turtle.penup()
            turtle.color("white")
            turtle.setpos(x=-20 * i, y=0)
            self.segments.append(turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def turn_left(self):
        self.head.left(TURN_90)

    def turn_right(self):
        self.head.right(TURN_90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)




