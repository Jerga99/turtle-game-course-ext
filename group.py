
from typing import TypeVar
from game_entity import GameEntity

T = TypeVar('T', bound=GameEntity)

class Group(list[T]):
    def __init__(self, collision_group: 'Group[T]'):
        super().__init__()
        self.collision_group = collision_group

    def update(self):
        for i, entity in enumerate(self):
            if entity.active:
                entity.update()
            else:
                entity.hideturtle()
                self.pop(i)

            if not self.collision_group is None:
                for other_entity in self.collision_group:
                    if entity.distance(other_entity.pos()) < 15:
                        other_entity.active = False
                        entity.active = False

    def restart(self):
        for entity in self:
            entity.hideturtle()

        self.clear()

