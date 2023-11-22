
from game_entity import GameEntity

class Group(list[GameEntity]):

    def update(self):
        for entity in self:
            entity.update()

    def restart(self):
        for entity in self:
            entity.hideturtle()

        self.clear()

