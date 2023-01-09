import random
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Coordinates:
    row_start: int
    row_end: int
    col_start: int
    col_end: int


class Ship:

    def __init__(self, length: int):
        self.length = length
        self.rotation = self.__set_ship_rotation()
        self.coordinates = self.__set_ship_coordinates()
        self.is_live = True

    def __set_ship_rotation(self) -> str:
        return random.choice(["horisontal", "vertical"]) if self.length > 1 else None

    def __set_ship_coordinates(self) -> Coordinates:
        if all([self.length > 1, self.rotation == "horisontal"]):
            row_start = random.randint(0, 5)
            row_end = row_start
            col_start = random.randint(0, 5 - self.length + 1)
            col_end = col_start + self.length - 1
        if all([self.length > 1, self.rotation == "vertical"]):
            row_start = random.randint(0, 5 - self.length + 1)
            row_end = row_start + self.length - 1
            col_start = random.randint(0, 5)
            col_end = col_start
        if self.length == 1:
            col_start = random.randint(0, 5)
            row_start = random.randint(0, 5)
            col_end, row_end = col_start, row_start
        return Coordinates(row_start, row_end, col_start, col_end)

    def __str__(self) -> str:
        return f"This ship loc at " \
               f"coordinates={self.coordinates}, " \
               f"len={self.length}, " \
               f"is_live={self.is_live}, " \
               f"rot={self.rotation}"


if __name__ == "__main__":
    ship = Ship(3)
    print(ship)
