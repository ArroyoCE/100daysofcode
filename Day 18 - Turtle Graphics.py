from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.shape("circle")
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)
x = -340
y = 300
for i in range(16):
    timmy.up()
    timmy.setposition(x, y)
    y -= 40
    for _ in range(18):
        timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.stamp()
        timmy.forward(40)

timmy.setposition(x, y + 40)

screen.exitonclick()
