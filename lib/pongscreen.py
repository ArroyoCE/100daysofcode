from turtle import Screen


class PongScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.screensize(800, 600)
        self.screen.bgcolor("black")
        self.screen.listen()
        self.screen.tracer(0)
        self.screen.title("Pong")



