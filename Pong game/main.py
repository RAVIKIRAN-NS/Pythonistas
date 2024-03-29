from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #collison with y_wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    #collision wih paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    #reset when  r_paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_points()
    #reset ball l_paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_points()

screen.exitonclick()
