import time
import turtle
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
screen.listen()
player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.onkey(player.turtle_move, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    # Detect collision with Cars
    for car_item in car.all_cars:
        if car_item.distance(player)<20:
            game_is_on = False
            scoreboard.game_over()

    #detect sucess cross
    if player.is_at_finished_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()


screen.exitonclick()
