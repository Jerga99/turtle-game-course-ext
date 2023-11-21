
import math
from turtle import Vec2D
from game_entity import GameEntity
from game_time import GameTime
import globals as g

def magnitude(vector: Vec2D):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)

def normalize(vector: Vec2D, mag: float):
    if mag > 0:
        return Vec2D(vector[0] / mag, vector[1] / mag)

    return vector

class Player(GameEntity):
    def __init__(self) -> None:
        super().__init__()
        self.color('#3ff6ff')
        self.shape('turtle')
        self.direction = Vec2D(0,0)
        self.movement_speed = 200 # pixels per second

    def set_direction(self, direction: Vec2D):
        self.direction = direction

    def take_damage(self):
        g.GAME_OVER = True

    def restart(self):
        self.home()

    def move(self):
        if self.direction == Vec2D(0,0):
            return

        position = self.pos()
        mag = magnitude(self.direction)
        normalized_dir = normalize(self.direction, mag)
        movement = normalized_dir * (self.movement_speed * GameTime.delta_time)

        target_angle = self.towards(self.pos() + normalized_dir)
        current_angle = self.heading()

        angle_difference = target_angle - current_angle
        angle_difference = (angle_difference + 180) % 360 - 180

        turn_step = 360 * GameTime.delta_time
        real_step = min(turn_step, abs(angle_difference))

        if angle_difference != 0:
            new_heading = current_angle + real_step * (1 if angle_difference > 0 else -1)
            self.setheading(new_heading)

        self.setpos(position + movement)

    def update(self):
        self.move()

