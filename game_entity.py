from turtle import Turtle

class GameEntity(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.shape('square')
        self.speed(0)
        self.penup()
        self.movement_speed = 150

    def take_damage(self):
        pass

    def restart(self):
        pass

    def update(self):
        pass
