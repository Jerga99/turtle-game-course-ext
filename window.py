
from turtle import Screen

class Window:
    def __init__(self) -> None:
        self.screen = Screen()
        self.screen.setup(800, 600)
        self.screen.title('Turtle Battles')
        self.screen.bgcolor('#000000')
        self.screen.tracer(0)
