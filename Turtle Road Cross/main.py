import time
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()
    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()
    #detection with top wall
    if player.is_at_finish_line() == True:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()