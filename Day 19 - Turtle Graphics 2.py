from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
screen = Screen()
screen.colormode(255)
screen.screensize(500, 400)
timmy.hideturtle()
turtles = []
choice = screen.textinput(title="Make your bet", prompt="Choose a Turtle from 1 to 6, which will win?")


def race():
    x = -230
    y = 180
    for _ in range(6):
        rafa = Turtle(shape="turtle")
        rafa.up()
        rafa.color(randint(0, 255), randint(0, 255), randint(0, 255))
        rafa.setposition(x, y)
        y -= 60
        turtles.append(rafa)
    if choice:
        race_on = True
    while race_on:
        for turtle in turtles:
            turtle.forward(randint(1, 10))
            if turtle.xcor() >= 230:
                winner = turtles.index(turtle)
                race_on = False

    if choice == winner + 1:
        print("Parabéns você ganhou.")
    else:
        print(f"Você errou, a tartaruga ganhadora é a número {winner + 1}")


def clear():
    timmy.clear()
    timmy.up()
    timmy.setposition(0, 0)
    timmy.down()


def move_forward():
    timmy.forward(10)
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))


def move_backwards():
    timmy.backward(10)
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))


def turn_right():
    timmy.right(15)
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))


def turn_left():
    timmy.left(15)
    timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))


race()

timmy.showturtle()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
