from turtle import Turtle, Screen

new_position = 0

class Paddle(Turtle):

    def __init__(self, coords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coords)


    def up(self):
        global new_position
        if self.ycor() < 240:
            new_position = self.ycor() + 20
            self.goto(self.xcor(), new_position)

    def down(self):
        global new_position
        if self.ycor() > -240:
            new_position = self.ycor() - 20
            self.goto(self.xcor(), new_position)
