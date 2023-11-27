
from typing import TypeVar
from game_entity import GameEntity

T = TypeVar('T', bound=GameEntity)

class Group(list[T]):

    def update(self):
        for i, entity in enumerate(self):
            if entity.active:
                entity.update()
            else:
                entity.hideturtle()
                self.pop(i)

    def restart(self):
        for entity in self:
            entity.hideturtle()

        self.clear()

