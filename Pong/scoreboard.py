from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.paddle_point = 0
        self.second_paddle_point = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.paddle_point, align="center", font=("Courier", 88, "normal"))
        self.goto(100, 200)
        self.write(
            self.second_paddle_point, align="center", font=("Courier", 88, "normal")
        )

    def paddle_score(self):
        self.paddle_point += 1
        self.update_scoreboard()

    def second_score(self):
        self.second_paddle_point += 1
        self.update_scoreboard()
