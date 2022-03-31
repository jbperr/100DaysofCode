from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xypos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xypos)

    def go_up(self):
        self.new_y = self.ycor() + 30
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 30
        self.goto(self.xcor(), self.new_y)
