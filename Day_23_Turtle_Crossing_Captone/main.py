import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

Screen().listen()
Screen().onkey(fun=player.move_forward, key="Up")

game_is_on = True

while game_is_on:
    time.sleep(player.level)
    screen.update()
    car_manager.create_car()

# Step 1 Turtle: Creation, Movement, and reset.
    if player.ycor() > 280:
        player.reset()
        score_board.level_up()


# Step 2 Creation of cars, Movement and deletion.
    for car in car_manager.all_cars:
        car_manager.move(car)
# Step 3 increase speed of cars when turtle is reset.
    # DONE
# Step 3 Collision with turtle and car: end game
    for car in car_manager.all_cars:
        if (player.ycor() > car.ycor() - 20 and player.ycor() < car.ycor() + 20 and player.xcor() > car.xcor() - 20
                and player.xcor() < car.xcor() + 20):
            score_board.game_over()
            game_is_on = False

# Step 4 Scoreboard: increase when turtle is reset.


screen.exitonclick()








