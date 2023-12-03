#####Turtle Intro######

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.pensize(2)
tim.speed(0)


# tim.forward(100)
# tim.backward(200)
# tim.right(90)
# tim.left(180)
# tim.setheading(0)


######## Challenge 1 - Draw a Square ############
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


######## Challenge 2 - Dashed line ############
# for i in range(1, 50):
#     tim.forward(10)
#     if i % 2:
#         tim.penup()
#     else:
#         tim.pendown()


######## Challenge 3 - 5 shapes ############
# for i in range(4, 10):
#     tim.color(random.random(), random.random(), random.random())
#     turn = 360/i
#     for k in range(i):
#         tim.forward(100)
#         tim.right(turn)
# ######## Challenge 4 - Random Walk ############
# directions = [0, 90, 180, 270]
# for i in range(1000):
#     tim.right(directions[random.randint(0, 3)])
#     tim.color(random.random(), random.random(), random.random())
#     tim.forward(50)
# ######## Challenge 5 - Spirograph ############
# size_of_gap = 3
# for i in range(360//size_of_gap):
#     tim.color(random.random(), random.random(), random.random())
#     tim.setheading(tim.heading() + size_of_gap)
#     tim.circle(100)

# ######## Challenge 6 - hirst painting ############

#extract colors from png
# import colorgram
# color_list = []
# colors = colorgram.extract('damien-hirst-severed-spots.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))
# print(color_list)

#TODO: 10x10, 20 in size spaced 50 paces
tim.penup()

tim.setheading(270)
tim.forward(350)
tim.setheading(0)
tim.forward(350)
color_list = [(252, 250, 247), (253, 247, 250), (237, 252, 245), (249, 228, 18), (212, 13, 9), (197, 12, 35), (231, 228, 5), (197, 69, 20), (32, 90, 188), (43, 212, 70), (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48), (240, 245, 251), (244, 39, 149), (65, 203, 229), (14, 205, 222), (63, 21, 10), (223, 20, 110), (229, 164, 9), (15, 154, 23), (245, 57, 16), (98, 75, 9), (248, 11, 9), (223, 139, 203), (67, 241, 160), (10, 97, 61), (5, 38, 33), (67, 219, 155)]
for i in range(10):
    tim.setheading(90)
    tim.forward(70)
    tim.setheading(180)
    tim.forward(700)
    tim.setheading(0)

    for j in range(10):
        # print dot
        random_color = random.choice(color_list)
        tim.color(random_color[0]/255, random_color[1]/255, random_color[2]/255)

        tim.pendown()
        # tim.begin_fill()
        # tim.circle(10)
        # tim.end_fill()
        tim.dot(20)
        tim.penup()
        tim.forward(70)


screen = Screen()
screen.exitonclick()
