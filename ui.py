
from turtle import Vec2D
from text import Text

class UI:
    def __init__(self, restart_callback, quit_callback) -> None:
        self.restart_text = Text('Restart?', Vec2D(0,0))

        self.accept_btn = Text('', Vec2D(0, -30))
        self.accept_btn.shape('square')
        self.accept_btn.shapesize(2, 5)
        self.accept_btn.color('green')
        self.accept_btn.onclick(restart_callback)

        self.decline_btn = Text('', Vec2D(0, -80))
        self.decline_btn.shape('square')
        self.decline_btn.shapesize(2, 5)
        self.decline_btn.color('red')
        self.decline_btn.onclick(quit_callback)

    def show_gameover(self):
        self.restart_text.show_text()
        self.accept_btn.showturtle()
        self.decline_btn.showturtle()

    def restart(self):
        self.restart_text.clear()
        self.accept_btn.hideturtle()
        self.decline_btn.hideturtle()
