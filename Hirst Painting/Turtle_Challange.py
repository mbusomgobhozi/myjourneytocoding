import turtle as t
import random

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# arrow = Turtle()

# arrow.shape("arrow")

# shapes = {
#     "triangle": 3,
#     "square": 4,
#     "pentagon": 5,
#     "hexagon": 6,
#     "heptagon": 7,
#     "octagon": 8,
#     "nonagon": 9,
#     "decagon": 10,
# }


# colors = ["blue", "red", "orange", "green", "pink", "purple", "yellow", "black"]
# # the thought was more of a grab how many sides there are to basically get the arrow to turn till it has created all the sides thats why there are two for loops the second one is to determine how many times it should turn before doing it again

# for i in shapes:
#     rand = random.choice(colors)
#     for _ in range(shapes[i]):
#         angle = 360 / shapes[i]
#         arrow.forward(100)
#         arrow.right(angle)
#         arrow.color(rand)


tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randin(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")


def draw_spirigraph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


screen = t.Screen()
screen.exitonclick()
