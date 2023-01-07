from ship import Ship


class Field:
    ship_quantity = {"3": 1, "2": 2, "1": 4}

    def __init__(self):
        self.empty_field = [[' ' for _ in range(6)] for _ in range(6)]
        self.ready_field = self.set_ready_field()

    def generate_ships(self):
        ships = [Ship(x, y, length) for ship in self.ship_quantity]
        return ships

    def set_ready_field(self):
        ships = self.generate_ships()
        return ...


