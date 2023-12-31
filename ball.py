from turtle import Turtle, Screen
import random
import time

screen = Screen()

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.penup()
        self.x_move = 10  # I can create my own attributes which are just variables with values
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.y_move *= -1  # I can just multiply the new attribute y_move by -1 to reverse it's movement downwards at the same angle

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed_l(self):
        self.x_move += 3

    def increase_speed_r(self):
        self.x_move -= 3









