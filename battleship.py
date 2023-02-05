import numpy as np

from field import Field
from gamers import Gamer, Player
from game_dataclasses import ShotCoordinates
from exceptions import *


class Battleship:

    def __init__(self, player1: str, player2: str):
        # create field objects and ships in them:
        self.player1_name = player1.upper()
        self.player2_name = player2.upper()

        self.player1_field = Field()
        self.player1_field.generate_ships()

        self.player2_field = Field()
        self.player2_field.generate_ships()

    def create_players(self) -> tuple[Gamer, Gamer]:
        # create players
        player1 = Player(self.player1_field, name=self.player1_name)
        player2 = Player(self.player2_field, name=self.player2_name)

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

        print(f"\n     {player.name} Field", ' ', ' ', ' ', ' ', f"   {player.opponent.name} Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6', ' ', ' ', ' ', ' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------', ' ', ' ', '  ---------------')

        for n, rows in enumerate(zip(player.player_field, hiding_field)):
            print(n + 1, '|', *rows[0], '|', ' ', ' ', n + 1, '|', *rows[1], '|')

        print('  ---------------', ' ', ' ', '  ---------------')

    @staticmethod
    def get_new_coordinates(player: Gamer) -> ShotCoordinates:
        while True:
            try:
                row, col = player.ask_coordinates()
                return ShotCoordinates(row - 1, col - 1)
            except CoordinatesException as e:
                print(e)
            except BusyCellOnFieldException as e:
                print(e)
            except InputTypeException as e:
                print(e)

    @staticmethod
    def check_ship_is_live(coordinates: ShotCoordinates, opponent: Gamer) -> None:
        row = coordinates.row
        col = coordinates.col
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
                print("THE SHIP IS KILLED!")
                break

    def make_shot(self, coordinates: ShotCoordinates, player: Gamer) -> bool:
        row = coordinates.row
        col = coordinates.col
        if player.opponent.player_field[row, col] == "O":
            player.opponent.player_field[row, col] = "X"
            print("THE SHIP IS DAMAGED")
            self.check_ship_is_live(coordinates, player.opponent)
            return True
        else:
            player.opponent.player_field[row, col] = "*"
            print("OVERSHOT!")
            return False

    @staticmethod
    def get_game_status(user_player: Gamer, ai_player: Gamer) -> str:
        if all((ship.is_killed for ship in user_player.ships)):
            return "AI WINS!"
        if all((ship.is_killed for ship in ai_player.ships)):
            return "USER WINS!"
        return "Game not finished"
