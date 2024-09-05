from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score_Board

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Score_Board()

game_loop = True

screen.listen()
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


while game_loop:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.update_score()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_loop = False
        score_board.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_loop = False
            score_board.game_over()


screen.exitonclick()
