import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_left()

    counter += 1
    if counter % cars.interval == 0:
        cars.create_a_car()

    if player.ycor() > 280:
        score.update_level()
        player.refresh()
        cars.refresh()

    for element in cars.cars:
        if player.distance(element) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
