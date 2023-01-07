import random
from dataclasses import dataclass


@dataclass
class ShipQuantity:
    length: int
    quantity: int


class Ship:

    def __init__(self, x: int, y: int, length: int):
        self.x = x
        self.y = y
        self.length = length
        self.rotation = self.set_ship_rotation()
        self.is_live = True

    def set_ship_rotation(self) -> str:
        if self.length > 1:
            return random.choice(["horisontal", "vertical"])

    def __str__(self):
        return f"This ship is at " \
               f"x={self.x}, " \
               f"y={self.y}, " \
               f"len={self.length}, " \
               f"is_live={self.is_live}, " \
               f"rot={self.rotation}"


if __name__ == "__main__":
    ship = Ship(1, 3, 4)
    print(ship)
