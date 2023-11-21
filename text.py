
from turtle import Turtle, Vec2D

class Text(Turtle):
    def __init__(self, text: str, pos: Vec2D ):
        super().__init__()
        self.color('white')
        self.penup()
        self.setpos(pos)
        self.hideturtle()
        self.text = text

    def show_text(self):
        self.write(self.text, font=('Arial', 15, 'normal'), align='center')
