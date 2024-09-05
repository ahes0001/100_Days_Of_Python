from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_COR_START_POS = 300
X_COR_END_POS = -300
Y_COR_TOP_SPAWN_BOUNDARY = 240
Y_COR_BOT_SPAWN_BOUNDARY = -240


class CarManager:
    def __init__(self):
        self.all_cars = []

    def move(self, car):
        car.forward(STARTING_MOVE_DISTANCE)

    def create_car(self):
        rand_num = random.randint(1,6)
        if rand_num == 6:
            car = Turtle()
            car.color(COLORS[random.randint(0, 5)])
            car.penup()
            car.shape("square")
            car.setheading(180)
            car.shapesize(1, 2)
            car.setpos(X_COR_START_POS, random.randint(Y_COR_BOT_SPAWN_BOUNDARY, Y_COR_TOP_SPAWN_BOUNDARY))
            self.all_cars.append(car)


