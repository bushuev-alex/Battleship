import numpy as np

from field import Field
from gamers import Gamer, Player
from game_dataclasses import ShotCoordinates
from exceptions import *


class Battleship:

    def __init__(self, player_lvl: str, opponent_lvl: str):
        # create field objects and ships in them:
        self.lvl1 = player_lvl
        self.lvl2 = opponent_lvl

        self.player1_name = f"1st ({player_lvl.upper()})"
        self.player2_name = f"2nd ({opponent_lvl.upper()})"

        self.player1_field = Field()
        self.player1_field.generate_ships()

        self.player2_field = Field()
        self.player2_field.generate_ships()

    def create_players(self) -> tuple[Gamer, Gamer]:
        # create players
        player1 = Player(self.player1_field, name=self.player1_name, level=self.lvl1)
        player2 = Player(self.player2_field, name=self.player2_name, level=self.lvl2)

        player1.set_opponent(player2)
        player2.set_opponent(player1)

        return player1, player2

    def greet(self) -> None:
        print("\n-----------------")
        print("  Greeting you   ")
        print("     in game     ")
        print("   Battleship    ")
        print("-----------------")
        print("   input format: ")
        print("      row col    ")
        print(" row = number 1-6 ")
        print(" col = number 1-6")
        print("-----------------\n")

    def draw_fields(self, player: Gamer) -> None:
        hiding_field = player.opponent.player_field.copy()
        hiding_field[hiding_field == "O"] = " "  # np.array

        print(f"\n", ' ' * 2, f"{player.name} Field", ' ' * 9, f"{player.opponent.name} Field")
        print(' ' * 7, '1', '2', '3', '4', '5', '6', ' ' * 19, '1', '2', '3', '4', '5', '6')
        print(' ' * 5, '---------------', ' ' * 15, '---------------')
        for n, rows in enumerate(zip(player.player_field, hiding_field)):
            print(' ' * 3, n + 1, '|', *rows[0], '|', ' ' * 13, n + 1, '|', *rows[1], '|')
        print(' ' * 5, '---------------',  ' ' * 15, '---------------')

    @staticmethod
    def get_new_coordinates(player: Gamer) -> ShotCoordinates:
        while True:
            try:
                row, col = player.ask_coordinates()
                return ShotCoordinates(row, col)
            except CoordinatesException as e:
                print(e)
            except BusyCellOnFieldException as e:
                print(e)
            except InputTypeException as e:
                print(e)

    @staticmethod
    def check_ship_is_dead(coordinates: ShotCoordinates, opponent: Gamer) -> bool:
        row = coordinates.row - 1
        col = coordinates.col - 1
        for ship in opponent.ships:
            # find right ship:
            condition = (row in range(ship.coordinates.row_start, ship.coordinates.row_end + 1) and
                         (col in range(ship.coordinates.col_start, ship.coordinates.col_end + 1)))
            if not condition:  # dot (row, col) not in ship's coordinates
                continue
            ship_dots: np.ndarray = ship.get_dots(opponent.player_field)
            if "O" not in ship_dots:  # all dots == "X"
                opponent.player_field[ship.coordinates.row_start:ship.coordinates.row_end + 1,
                                      ship.coordinates.col_start:ship.coordinates.col_end + 1] = "■"
                ship.is_killed = True
                return True
        return False

    def make_shot(self, coordinates: ShotCoordinates, player: Gamer) -> [ShotCoordinates|bool]:
        row = coordinates.row - 1
        col = coordinates.col - 1
        if player.opponent.player_field[row, col] == "O":
            player.opponent.player_field[row, col] = "X"
            print("THE SHIP IS DAMAGED")
            if self.check_ship_is_dead(coordinates, player.opponent):
                print("THE SHIP IS KILLED!")
                player.successful_shot = None
                return coordinates
            player.successful_shot = coordinates
            return coordinates
        else:
            player.opponent.player_field[row, col] = "*"
            player.successful_shot = None
            print("OVERSHOT!")
            return False

    @staticmethod
    def get_game_status(player_1: Gamer, player_2: Gamer) -> str:
        if all((ship.is_killed for ship in player_1.ships)):
            return f"{player_2.name} WINS!"
        if all((ship.is_killed for ship in player_2.ships)):
            return f"{player_1.name} WINS!"
        return "Game not finished"
