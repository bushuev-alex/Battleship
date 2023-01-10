import random

from field import Field
from ship import Ship


class Gamer:

    def __init__(self, user_field: Field, ai_field: Field):
        self.player_field = None
        self.opponent_field = None
        self.hiding_field = None
        self.ships = None

    def ask_coordinates(self):
        pass


class UserGamer(Gamer):

    def __init__(self, user_field: Field, ai_field: Field):
        super().__init__(user_field, ai_field)
        self.player_field = user_field.field
        self.opponent_field = ai_field.field
        self.hiding_field = ai_field.hiding_field
        self.ships = user_field.ships

    def ask_coordinates(self):
        super().ask_coordinates()
        x, y = [int(i) for i in input("Enter shot coordinates: ").split()]
        return x, y


class AIGamer(Gamer):

    def __init__(self, user_field: Field, ai_field: Field):
        super().__init__(user_field, ai_field)
        self.player_field = ai_field.field
        self.opponent_field = user_field.field
        self.hiding_field = user_field.hiding_field
        self.ships = ai_field.ships

    def ask_coordinates(self):
        super().ask_coordinates()
        x, y = random.randint(1, 6), random.randint(1, 6)
        print(f"AI shot coordinates: {x}, {y}")
        return x, y


if __name__ == "__main__":
    user_field_obj = Field()
    user_field_obj.generate_ships()

    ai_field_obj = Field()
    ai_field_obj.generate_ships()

    user_player = UserGamer(user_field_obj, ai_field_obj)
    ai_player = AIGamer(user_field_obj, ai_field_obj)

    print(user_player.player_field, ai_player.opponent_field, sep=' \t')

