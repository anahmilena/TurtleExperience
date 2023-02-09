from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = 0
        self.interval = 6

    def create_a_car(self):
        new_car = Turtle(shape="triangle")
        new_car.setheading(180)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.goto(280, random.randint(-225, 250))
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        self.cars.append(new_car)

    def move_left(self):
        for element in self.cars:
            element.setx(element.xcor() - STARTING_MOVE_DISTANCE - self.car_speed)

    def refresh(self):
        for element in self.cars:
            element.goto(1000, 1000)
        print(self.cars)
        self.cars.clear()
        print(self.cars)
        self.car_speed += MOVE_INCREMENT
        self.interval -= 1
