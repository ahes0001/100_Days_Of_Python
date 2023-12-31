from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 100
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("blue")
        self.goto(STARTING_POSITION)
        self.level = 0.1

    def move_forward(self):
        self.forward(10)

    def reset(self):
        self.goto(STARTING_POSITION)
        self.level *= 0.7
