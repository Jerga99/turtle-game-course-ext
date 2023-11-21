from turtle import Vec2D
from player import Player

def handle_movement(*keys, player: Player):
    (w,a,s,d) = keys

    directions = [Vec2D(0,0), Vec2D(0,0)]

    if w.down:
        directions.append(Vec2D(0,1))
    if s.down:
        directions.append(Vec2D(0,-1))
    if a.down:
        directions.append(Vec2D(-1,0))
    if d.down:
        directions.append(Vec2D(1,0))

    last_two = directions[-2:]
    direction = last_two[0] + last_two[1]
    player.set_direction(direction)
