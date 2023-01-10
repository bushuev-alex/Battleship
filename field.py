from ship import Ship
import numpy as np


class Field:

    def __init__(self):
        self.ship_quantity = {"3": 1, "2": 2, "1": 4}
        self.field = np.asarray([[' ' for _ in range(6)] for _ in range(6)])
        self.hiding_field = np.asarray([[' ' for _ in range(6)] for _ in range(6)])
        self.ships = []

    def __check_border_around_ship(self, ship: Ship) -> bool:
        field = np.asarray([[' ' for _ in range(8)] for _ in range(8)])  # create field 8x8
        field[1:7, 1:7] = self.field  # insert field 6x6 in field 8x8 to make empty borders
        col_left = field[ship.coordinates.row_start+1-1:ship.coordinates.row_end+1+2,
                         ship.coordinates.col_start+1-1]
        col_right = field[ship.coordinates.row_start+1-1:ship.coordinates.row_end+1+2,
                          ship.coordinates.col_end+1+1]
        row_upper = field[ship.coordinates.row_start+1-1,
                          ship.coordinates.col_start+1-1:ship.coordinates.col_end+1+2]
        row_lower = field[ship.coordinates.row_end+1+1,
                          ship.coordinates.col_start+1-1:ship.coordinates.col_end+1+2]
        border_lines = list(col_left) + list(col_right) + list(row_upper) + list(row_lower)
        if all(map(lambda x: x == " ", border_lines)):
            return True
        return False

    def __insert_ship_in_field(self, ship: Ship) -> None:
        self.field[ship.coordinates.row_start:ship.coordinates.row_end + 1,
                   ship.coordinates.col_start:ship.coordinates.col_end + 1] = "O"

    def __check_cell_is_busy(self, ship: Ship) -> bool:
        if self.field[ship.coordinates.row_start, ship.coordinates.col_start] == "O":
            return True
        return False

    def generate_ships(self):
        for ship_length in self.ship_quantity:
            for quantity in range(self.ship_quantity.get(ship_length)):
                n = 0
                while True:
                    ship = Ship(int(ship_length))
                    if self.__check_cell_is_busy(ship):
                        continue
                    if self.__check_border_around_ship(ship):
                        self.__insert_ship_in_field(ship)
                        self.ships.append(ship)
                        break
                    n += 1
                    if n > 30:  # check if there is no proper place for next ship / infinite cycle
                        self.field = np.asarray([[' ' for _ in range(6)] for _ in range(6)])
                        return self.generate_ships()


if __name__ == "__main__":
    field = Field()
    field.generate_ships()
    print(field.field)
