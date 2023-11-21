
from turtle import onkeypress, onkeyrelease

class WatchedKey:
    def __init__(self, key: str) -> None:
        self.key = key
        self.down = False
        onkeypress(self.press, key)
        onkeyrelease(self.release, key)

    def press(self):
        self.down = True

    def release(self):
        self.down = False
