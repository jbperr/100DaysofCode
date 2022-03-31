from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # top and bot collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # paddle collision
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 330
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -330
    ):
        ball.bounce_x()

    # right paddle miss
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    # left paddle miss
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

    if scoreboard.l_score > 2 or scoreboard.r_score > 2:
        scoreboard.gameover()
        game_is_on = False

screen.exitonclick()
