from turtle import Turtle
FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-200, 250)
GAME_OVER_POSITION = (0, 0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0

        self.write_scores()

    def write_scores(self) -> object:
        self.goto(SCORE_POSITION)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_scores()

    def game_over(self):
        self.goto(GAME_OVER_POSITION)
        self.write("GAME OVER!", align="center", font=FONT)
