from turtle import Turtle
FONT = ('Courier', 24, 'normal')
CENTER_ALIGN = "center"


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write_title()
        self.hideturtle()

    def write_title(self):
        self.write(arg=f"Score: {self.score}", align=CENTER_ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_title()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", align=CENTER_ALIGN, font=FONT)

