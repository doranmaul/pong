from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, key="Up")
screen.onkey(r_paddle.down, key="Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

game_is_on = True

while game_is_on:
    time.sleep(0.08)
    screen.update()
    ball.move_ball()
    print(ball.x_move)

    # Detect collision with wall

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.increase_speed_r()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.increase_speed_l()

    # Detect if r_paddle misses ball

    if ball.xcor() > 380:
        ball.x_move = 10
        ball.reset_position()
        score.l_point()


    # Detect if l_paddle misses ball

    if ball.xcor() < -390:
        ball.x_move = -10
        ball.reset_position()
        score.r_point()















screen.exitonclick()

