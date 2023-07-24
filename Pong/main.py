from paddle import Paddle
from turtle import Screen
from ball import Ball
import time
from scoreboard import Scoreboard

# seup the screen first before initializing the paddle
screen = Screen()
screen.setup(width=600, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create paddles, ball and scoreboard
paddle = Paddle((350, 0))
second_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
screen.onkey(second_paddle.go_up, "w")
screen.onkey(second_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall please note a class method could have been used here
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Call the bounce method
        ball.bounce_y()
    # Detect collision with the paddles
    if (
        ball.distance(paddle) < 50
        and ball.xcor() > 320
        or ball.distance(second_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Now for the rules right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.paddle_score()

    # left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.second_score()


screen.exitonclick()
