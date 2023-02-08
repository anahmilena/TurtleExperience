from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270, 270)
        self.level = 1
        self.hideturtle()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=FONT, align="center")

