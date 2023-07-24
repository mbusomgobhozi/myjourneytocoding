from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.start()

    def start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        # y_axis = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), y_axis)
        self.forward(MOVE_DISTANCE)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
