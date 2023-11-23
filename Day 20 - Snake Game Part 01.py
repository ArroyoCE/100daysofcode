from turtle import Screen, Turtle
from random import randint
from time import sleep


def check_cordinates(c, snake):
    for num in range(len(snake)):
        if snake[num].pos() == c:
            return True
    return False


def append_turtle(w):
    p = Turtle()
    p.up()
    p.shape("square")
    p.resizemode("user")
    p.turtlesize(0.5, 0.5, 1)
    p.color("white")
    p.setposition(w)
    return p


def check_position(turtle):
    for n in range(0, len(snake_body)):
        if snake_body[n].pos() == turtle.pos():
            return False
    return True


def check_bounds():
    if snake_body[0].xcor() == 280 or snake_body[0].xcor() == -280:
        return False
    elif snake_body[0].ycor() == 280 or snake_body[0].ycor() == -280:
        return False
    else:
        return True


def check_touch(snake):
    for number in range(1, len(snake)):
        if snake[0].pos() == snake[number].pos():
            return False

    return True


def move_north():
    if snake_body[0].heading() != 270:
        snake_body[0].setheading(90)


def move_south():
    if snake_body[0].heading() != 90:
        snake_body[0].setheading(270)


def move_left():
    if snake_body[0].heading() != 0:
        snake_body[0].setheading(180)


def move_right():
    if snake_body[0].heading() != 180:
        snake_body[0].setheading(0)


snake_body = []
y = 0
x = 0
score = 0

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.onkey(key="w", fun=move_north)
screen.onkey(key="s", fun=move_south)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)

screen.title("Snake Game")

for _ in range(3):
    t = Turtle()
    t.up()
    t.setposition(x, y)
    t.color("white")
    t.shape("square")
    t.resizemode("user")
    t.speed("fast")
    t.turtlesize(0.5, 0.5, 1)
    snake_body.append(t)
    x -= 10
    screen.update()
    sleep(0.1)

size = len(snake_body)
x = Turtle()
x.up()
x.ht()
x.setposition((randint(-28, 28) * 10.0, randint(-28, 28) * 10.0))
while check_cordinates(x.pos(), snake_body):
    x.setposition((randint(-28, 28) * 10, randint(-28, 28) * 10.0))

x.shape("circle")
x.resizemode("user")
x.turtlesize(0.5, 0.5, 1)
x.color("blue")
x.showturtle()


while check_bounds() and check_touch(snake_body):
    screen.update()
    sleep(0.1)
    if len(snake_body) > size:
        x.setposition((randint(-26, 26) * 10.0, randint(-26, 26) * 10.0))
        while check_cordinates(x.pos(), snake_body):
            x.setposition((randint(-28, 28) * 10, randint(-28, 28) * 10))
        x.showturtle()
        size = len(snake_body)

    pos = snake_body[0].pos()
    snake_body[0].forward(10)
    for i in range(1, len(snake_body)):
        pos2 = snake_body[i].pos()
        snake_body[i].setposition(pos)
        pos = pos2
    screen.update()
    sleep(0.005)
    print(x.pos())

    if x.distance(snake_body[0]) < 5:
        snake_body.append(append_turtle(pos2))
        x.ht()
        screen.update()
        sleep(0.1)

screen.exitonclick()
