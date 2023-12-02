from turtle import Screen, Turtle
import random


screen = Screen()

# ########### ETCH SKETCH ###############
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_clock_wise():
#     tim.setheading(tim.heading()+10)
#
#
# def turn_counter_clock_wise():
#     tim.setheading(tim.heading()-10)
#
#
# def clear_and_center():
#     screen.resetscreen()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=turn_counter_clock_wise)
# screen.onkey(key="a", fun=turn_clock_wise)
# screen.onkey(key="c", fun=clear_and_center)

# ########### Turtle Race ##############
is_race_on = True
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

all_turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-230, -80+40*i)
    all_turtles.append(turtle)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()

