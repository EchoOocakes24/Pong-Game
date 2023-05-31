# Day22-100-Days-of-Python

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(370, 0)
r_paddle = Paddle(-370, 0)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(l_paddle.up, "Up")
screen.onkey(l_paddle.down, "Down")

screen.onkey(r_paddle.up, "w")
screen.onkey(r_paddle.down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.xcor() > 330 and ball.distance(l_paddle) < 50 or ball.xcor() < -330 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()
