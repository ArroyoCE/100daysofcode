from turtle import Turtle

class Paddle:
    def __init__(self, a):
        self.paddle = Turtle()
        self.paddle.shape("square")
        self.paddle.resizemode("user")
        self.paddle.color("white")
        self.paddle.turtlesize(4, 0.5, 4)
        self.paddle.up()
        self.paddle.setheading(0)
        if a == 1:
            self.paddle.setposition(-360, 0)
        elif a == 2:
            self.paddle.setposition(360, 0)

    def move_up(self):
        if self.paddle.ycor() != 260:
            self.paddle.setposition(self.paddle.xcor(), self.paddle.ycor()+10)

    def move_down(self):
        if self.paddle.ycor() != -260:
            self.paddle.setposition(self.paddle.xcor(), self.paddle.ycor()-10)
