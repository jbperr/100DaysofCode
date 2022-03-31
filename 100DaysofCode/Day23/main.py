from concurrent.futures import wait
import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtlist = []
player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()


    if player.ycor() >= 280:
        player.next_level()
        scoreboard.update_level()
        car.level_up()
    
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
screen.exitonclick()
