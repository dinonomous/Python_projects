import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.listen()

screen.tracer(0)
player = Player()
scorebord = Scoreboard()
game_is_on = True
car = CarManager()
while game_is_on:
    time.sleep(0.1)
    car.create_car()
    car.move()
    screen.onkey(player.move, "Up")
    screen.update()

    for i in car.all_cars:
        if i.distance(player)<30:
            scorebord.game_over()
            game_is_on = False

    if player.won():
        player.go_to_start()
        car.changeSpeed()
        scorebord.increase_level()
screen.exitonclick()