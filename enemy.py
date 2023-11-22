import random
from turtle import Vec2D
from game_entity import GameEntity
from game_time import GameTime

SPAWN_RANGE = 120

class Enemy(GameEntity):
    def __init__(self, pos: Vec2D, target: GameEntity):
        super().__init__()
        self.target = target
        self.setpos(pos)
        self.timer = 0
        self.jump_interval = 3

    def follow_target(self):
        target_post = self.target.pos()
        new_heading = self.towards(target_post)
        self.setheading(new_heading)
        self.forward(self.movement_speed * GameTime.delta_time)

    def restart(self):
        self.setpos(200,200)

    def update(self):
        self.timer += GameTime.delta_time

        if self.timer >= self.jump_interval:
            self.timer = 0
            self.jump_interval = random.randint(2, 5)
            x = random.randint(-SPAWN_RANGE, SPAWN_RANGE)
            y = SPAWN_RANGE if random.randint(0,1) == 0 else -SPAWN_RANGE
            jump_position = self.target.pos() + (x, y)
            self.teleport(*jump_position)

        if self.distance(self.target.pos()) <= 15:
            self.target.take_damage()

        self.follow_target()
