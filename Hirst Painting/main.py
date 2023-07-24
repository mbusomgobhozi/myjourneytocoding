import colorgram
import turtle as turtle_module
import random

# colors = colorgram.extract("hirst_image.jpg", 30)

rgb_colors = [
    (226, 229, 235),
    (244, 237, 222),
    (243, 234, 240),
    (232, 242, 237),
    (192, 165, 115),
    (138, 166, 190),
    (56, 102, 140),
    (141, 91, 50),
    (12, 23, 55),
    (222, 207, 123),
    (182, 154, 42),
    (61, 22, 11),
    (182, 146, 165),
    (142, 177, 151),
    (72, 117, 81),
    (58, 15, 26),
    (126, 79, 102),
    (130, 30, 16),
    (15, 39, 23),
    (24, 53, 127),
    (177, 188, 215),
    (164, 104, 134),
    (115, 31, 46),
    (97, 150, 100),
    (98, 121, 172),
    (210, 178, 197),
    (174, 105, 93),
    (74, 150, 165),
    (25, 91, 65),
    (172, 205, 180),
]

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

# setting the position of the dot to be in the middle
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dots = 100

# the for loop is to just keep the code running untill 100 dots are generated

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)
    # this line is to just reset to the start if the dot count gets to 10
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
