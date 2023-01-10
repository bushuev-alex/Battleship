import random
import numpy as np
from game_dataclasses import ShipCoordinates


class Ship:

    def __init__(self, length: int):
        self.length = length
        self.rotation = self.__set_ship_rotation()
        self.coordinates = self.__set_ship_coordinates()
        self.is_live = True

    def __set_ship_rotation(self) -> str:
        return random.choice(["horisontal", "vertical"]) if self.length > 1 else None

    def __set_ship_coordinates(self) -> ShipCoordinates:
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
        return ShipCoordinates(row_start, row_end, col_start, col_end)

    def get_dots(self, field: np.ndarray) -> str:
        return "".join(field[self.coordinates.row_start:self.coordinates.row_end+1,
                             self.coordinates.col_start:self.coordinates.col_end+1][0])

    def __str__(self) -> str:
        return f"This ship loc at " \
               f"coordinates={self.coordinates}, " \
               f"len={self.length}, " \
               f"is_live={self.is_live}, " \
               f"rot={self.rotation}"


if __name__ == "__main__":
    ship = Ship(3)
    print(ship)