from abc import ABC
import random
from field import Field
from game_dataclasses import ShotCoordinates
from exceptions import *
from typing import Union


class Gamer(ABC):

    def __init__(self, player_field: Field, name: str, level: str):
        self.player_field = player_field.field
        self.ships = player_field.ships
        self.name = name
        self.opponent: Gamer
        self.lvl = level
        self.successful_shot: Union[ShotCoordinates | None] = None

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
        match self.lvl:
            case "user":
                return self.ask_user_coordinates()
            case "easy_ai":
                return self.ask_easy_ai_coordinates()
            case "medium_ai":
                return self.ask_medium_ai_coordinates()
            case "hard_ai":
                return self.ask_hard_ai_coordinates()

    def ask_user_coordinates(self) -> ShotCoordinates:
        try:
            row, col = [int(i) for i in input("Enter shot coordinates: ").split()]
            if not (1 <= row <= 6 and 1 <= col <= 6):
                raise CoordinatesException
            if self.opponent.player_field[row - 1, col - 1] in ['X', '*', "■"]:
                raise BusyCellOnFieldException
            return ShotCoordinates(row, col)
        except ValueError:
            raise InputTypeException

    def ask_easy_ai_coordinates(self) -> ShotCoordinates:
        row, col = random.randint(1, 6), random.randint(1, 6)
        if self.opponent.player_field[row - 1, col - 1] in ['X', '*', "■"]:
            raise BusyCellOnFieldException
        print(f"AI shot coordinates: {row}, {col}")
        return ShotCoordinates(row, col)

    def ask_medium_ai_coordinates(self) -> ShotCoordinates:
        if not self.successful_shot:
            row, col = random.randint(1, 6), random.randint(1, 6)
        else:
            row, col = self.get_border_dots()
        if self.opponent.player_field[row - 1, col - 1] in ['X', '*', "■"]:
            raise BusyCellOnFieldException
        print(f"AI shot coordinates: {row}, {col}")
        return ShotCoordinates(row, col)

    def ask_hard_ai_coordinates(self) -> ShotCoordinates:
        pass

    def get_border_dots(self) -> tuple:
        row_down = self.successful_shot.row - 1
        if row_down == 0:
            row_down = 1
        row_up = self.successful_shot.row + 1
        if row_up == 7:
            row_up = 6

        col_left = self.successful_shot.col - 1
        if col_left == 0:
            col_left = 1
        col_right = self.successful_shot.col + 1
        if col_right == 7:
            col_right = 6

        dot_l = (self.successful_shot.row, col_left)
        dot_r = (self.successful_shot.row, col_right)
        dot_down = (row_down, self.successful_shot.col)
        dot_up = (row_up, self.successful_shot.col)

        random_dot = random.choice([dot_l, dot_r, dot_down, dot_up])

        if all([self.opponent.player_field[*(x - 1 for x in dot_l)] in ['X', '*', "■"],
               self.opponent.player_field[*(x - 1 for x in dot_r)] in ['X', '*', "■"],
               self.opponent.player_field[*(x - 1 for x in dot_down)] in ['X', '*', "■"],
               self.opponent.player_field[*(x - 1 for x in dot_up)] in ['X', '*', "■"]]
               ):
            row, col = random.randint(1, 6), random.randint(1, 6)
            return row, col

        # print(self.opponent.player_field, self.successful_shot, random_dot)
        return random_dot



if __name__ == "__main__":
    user_field_obj = Field()
    user_field_obj.generate_ships()

    ai_field_obj = Field()
    ai_field_obj.generate_ships()

    user_player = Player(user_field_obj, "USER")
    ai_player = Player(ai_field_obj, "MEDIUM_AI")

    print(user_player)
    print(ai_player)
