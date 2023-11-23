from lib.pongscreen import PongScreen
from lib.pongpaddle import Paddle
from lib.pongball import Ball
from time import sleep
s = PongScreen()

ball = Ball()
p1 = Paddle(1)
p2 = Paddle(2)
is_alive = True
s.screen.onkeypress(key="Up", fun=p1.move_up)
s.screen.onkeypress(key="Down", fun=p1.move_down)
s.screen.onkeypress(key="w", fun=p2.move_up)
s.screen.onkeypress(key="s", fun=p2.move_down)

while is_alive:

    ball.move(p1.paddle, p2.paddle)
    s.screen.update()
    sleep(0.03)


s.screen.exitonclick()

