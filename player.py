
import math
from tkinter import Event
from turtle import Vec2D, window_height, window_width
from game_entity import GameEntity
from game_time import GameTime
from projectile import Projectile
from group import Group
import globals as g

def magnitude(vector: Vec2D):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)

def normalize(vector: Vec2D, mag: float):
    if mag > 0:
        return Vec2D(vector[0] / mag, vector[1] / mag)

    return vector

class Player(GameEntity):
    def __init__(self, projectiles: Group[Projectile]) -> None:
        super().__init__()
        self.color('#3ff6ff')
        self.shape('turtle')
        self.direction = Vec2D(0,0)
        self.projectiles = projectiles
        self.movement_speed = 200 # pixels per second
        self.mouse_pos = Vec2D(0,0)

    def on_mouse_movement(self, event: Event):
        x = event.x - window_width() / 2
        y = window_height() / 2 - event.y
        self.mouse_pos = Vec2D(x,y)

    def spawn_projectile(self):
        projectile = Projectile(self.pos(), self.mouse_pos)
        self.projectiles.append(projectile)

    def set_direction(self, direction: Vec2D):
        self.direction = direction

    def take_damage(self):
        g.GAME_OVER = True

    def restart(self):
        self.projectiles.restart()
        self.home()

    def move(self):
        if self.direction == Vec2D(0,0):
            return

        position = self.pos()
        mag = magnitude(self.direction)
        normalized_dir = normalize(self.direction, mag)
        movement = normalized_dir * (self.movement_speed * GameTime.delta_time)

        target_angle = self.towards(self.mouse_pos)
        self.setheading(target_angle)

        self.setpos(position + movement)

    def update(self):
        self.move()
        self.projectiles.update()

