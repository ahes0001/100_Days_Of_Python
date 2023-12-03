import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

Screen().listen()
Screen().onkey(fun=player.move_forward, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

# Step 1 Turtle: Creation, Movement, and reset.
    if player.ycor() > 280:
        player.reset()
# Step 2 Creation of cars, Movement and deletion.

# Step 3 increase speed of cars when turtle is reset.
# Step 3 Collision with turtle and car: end game
# Step 4 Scoreboard: increase when turtle is reset.








