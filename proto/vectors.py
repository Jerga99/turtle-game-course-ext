
from turtle import Vec2D

player_pos = Vec2D(2,3)

_dir = Vec2D(5,2)

movement = player_pos + _dir

print(f'index 0: {movement[0]}')
print(f'index 1: {movement[1]}')
