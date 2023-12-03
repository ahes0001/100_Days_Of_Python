from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed(1)
        self.x_movement = 5
        self.y_movement = 5
        self.move_speed = 0.02

    def move(self):
        self.goto(self.xcor() + self.x_movement, self.ycor() + self.y_movement)

    def bounce_ver(self):
        self.y_movement *= -1

    def bounce_paddle(self):
        self.x_movement *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.bounce_ver()
        self.move_speed = 0.02
