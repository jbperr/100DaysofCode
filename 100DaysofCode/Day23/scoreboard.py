from turtle import Turtle

FONT = ("Courier", 24, "normal")
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.hideturtle()
        self.level = 0
        self.colorpos = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.color(COLORS[self.colorpos])
        self.level += 1
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

        if self.colorpos < 5:
            self.colorpos += 1
        elif self.colorpos == 5:
            self.colorpos = 0
