from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_turtle()
        scoreboard.increase_score()
    #collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #collision with tail
    for first_turtle in snake.all_turtles[1:]:
        if snake.head.distance(first_turtle) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()



