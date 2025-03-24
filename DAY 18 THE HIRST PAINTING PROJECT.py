import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed(10)
tim.penup()
tim.hideturtle()
color_list = [(244, 229, 50), (6, 37, 28), (237, 228, 2), (193, 67, 24), (221, 151, 81), (36, 210, 91), (240, 41, 122),
              (35, 92, 177), (32, 31, 156), (205, 11, 5), (16, 18, 53), (92, 185, 218), (64, 9, 44),
              (231, 156, 6), (58, 21, 10), (206, 31, 94), (219, 134, 178), (12, 201, 221), (18, 149, 28),
              (90, 237, 168), (237, 58, 31), (81, 212, 150), (96, 75, 9), (238, 160, 199), (87, 87, 206),
              ]

tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)