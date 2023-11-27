
from turtle import Vec2D
from game_entity import GameEntity
from game_time import GameTime

class Projectile(GameEntity):
    def __init__(self, pos: Vec2D, direction: Vec2D) -> None:
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.setpos(pos)
        self.setheading(self.towards(pos + direction))
        self.movement_speed = 300
        self.max_life_time = 0.5
        self.current_life_time = 0

    def update(self):
        self.current_life_time += GameTime.delta_time

        if self.current_life_time >= self.max_life_time:
            self.active = False
        else:
            self.forward(self.movement_speed * GameTime.delta_time)
