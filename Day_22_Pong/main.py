from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Score_Board

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score_board = Score_Board()


screen.listen()
screen.onkey(key="Up", fun=paddle_right.up)
screen.onkey(key="Down", fun=paddle_right.down)

screen.onkey(key="w", fun=paddle_left.up)
screen.onkey(key="s", fun=paddle_left.down)

game_loop = True

while game_loop:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ver()

    # Detect collision with paddles
    if (ball.xcor() > 320 and paddle_right.distance(ball) < 60
            or ball.xcor() < -320 and paddle_left.distance(ball) < 60):
        ball.bounce_paddle()

    # Detect ball if out of bounds and reset ball

    if ball.xcor() > 380:
        ball.reset()
        score_board.l_point()

    if ball.xcor() < -380:
        ball.reset()
        score_board.r_point()











screen.exitonclick()