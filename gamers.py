import random
from field import Field
from game_dataclasses import ShotCoordinates


class Gamer:

    def __init__(self, player_field: Field):
        self.player_field = None
        self.ships = None
        self.name = None
        self.opponent = None

    def set_opponent(self, opponent):
        self.opponent = opponent

    def ask_coordinates(self) -> ShotCoordinates:
        pass


class UserGamer(Gamer):

    def __init__(self, user_field: Field):
        super().__init__(user_field)
        self.player_field = user_field.field
        self.ships = user_field.ships
        self.name = "USER"
        self.opponent = None

    def ask_coordinates(self) -> ShotCoordinates:
        x, y = [int(i) for i in input("Enter shot coordinates: ").split()]
        return ShotCoordinates(x, y)

    def __str__(self):
        return f"name = {self.name}\n" \
               f"player_field = \n{self.player_field}\n" \
               f"ships = \n{self.ships}\n"


class AIGamer(Gamer):

    def __init__(self, ai_field: Field):
        super().__init__(ai_field)
        self.player_field = ai_field.field
        self.ships = ai_field.ships
        self.name = "AI"
        self.opponent = None

    def ask_coordinates(self) -> ShotCoordinates:
        x, y = random.randint(1, 6), random.randint(1, 6)
        print(f"AI shot coordinates: {x}, {y}")
        return ShotCoordinates(x, y)

    def __str__(self):
        return f"name = {self.name}\n" \
               f"player_field = \n{self.player_field}\n" \
               f"ships = \n{self.ships}\n"


if __name__ == "__main__":
    user_field_obj = Field()
    user_field_obj.generate_ships()

    ai_field_obj = Field()
    ai_field_obj.generate_ships()

    user_player = UserGamer(user_field_obj)
    ai_player = AIGamer(ai_field_obj)

    print(user_player)
    print(ai_player)
