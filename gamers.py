from abc import ABC
import random
from field import Field
from game_dataclasses import ShotCoordinates
from exceptions import *


class Gamer(ABC):

    def __init__(self, player_field: Field, name: str):
        self.player_field = player_field.field
        self.ships = player_field.ships
        self.name = name
        self.opponent: Gamer

    def set_opponent(self, opponent) -> None:
        self.opponent = opponent

    def ask_coordinates(self) -> ShotCoordinates:
        pass

    def __str__(self):
        return f"name = {self.name}\n" \
               f"player_field = \n{self.player_field}\n" \
               f"ships = \n{self.ships}\n"


class Player(Gamer):

    def ask_coordinates(self) -> ShotCoordinates:
        match self.name:
            case "USER":
                try:
                    row, col = [int(i) for i in input("Enter shot coordinates: ").split()]
                    if not (1 <= row <= 6 and 1 <= col <= 6):
                        raise CoordinatesException
                    if self.opponent.player_field[row - 1, col - 1] in ['X', '*', "■"]:
                        raise BusyCellOnFieldException
                    return ShotCoordinates(row, col)
                except ValueError:
                    raise InputTypeException
            case "EASY_AI":
                row, col = random.randint(1, 6), random.randint(1, 6)
                print(f"AI shot coordinates: {row}, {col}")
                return ShotCoordinates(row, col)
            case "MEDIUM_AI":
                row, col = random.randint(1, 6), random.randint(1, 6)
                print(f"AI shot coordinates: {row}, {col}")
                return ShotCoordinates(row, col)


if __name__ == "__main__":
    user_field_obj = Field()
    user_field_obj.generate_ships()

    ai_field_obj = Field()
    ai_field_obj.generate_ships()

    user_player = Player(user_field_obj, "USER")
    ai_player = Player(ai_field_obj, "MEDIUM_AI")

    print(user_player)
    print(ai_player)
