from turtle import Turtle

LEFT_POSITION = (-100, 200)
RIGHT_POSITION = (100, 200)


class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.write_scores()

    def write_scores(self):
        self.goto(LEFT_POSITION)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(RIGHT_POSITION)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.write_scores()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.write_scores()
