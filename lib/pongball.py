from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.shape("circle")
        self.turtlesize(0.7, 0.7, 0.5)
        self.ymove = 5
        self.xmove = 5

    def move_ball(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def move(self, p1, p2):
        if self.xcor() <= -360 and self.distance(p1) <= 45:
            self.xmove *= -1
            self.move_ball()


        elif self.xcor() >= 360 and self.distance(p2) <= 45:
            self.xmove *= -1
            self.move_ball()

        elif self.ycor() >= 260 or self.ycor() <= -260:
            print(self.heading())
            self.ymove *= -1
            self.move_ball()

        else:
            self.move_ball()
