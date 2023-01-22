import numpy as np

from field import Field
from gamers import Gamer, UserGamer, AIGamer
from game_dataclasses import ShotCoordinates
from exceptions import *


class Battleship:

    def __init__(self):
        # create field objects and ships in them:
        self.user_field = Field()
        self.user_field.generate_ships()
        self.ai_field = Field()
        self.ai_field.generate_ships()

    def create_players(self) -> tuple[Gamer, Gamer]:
        # create players
        user_player = UserGamer(self.user_field)
        ai_player = AIGamer(self.ai_field)

        user_player.set_opponent(ai_player)
        ai_player.set_opponent(user_player)

        return user_player, ai_player

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

                if not (1 <= row <= 6 and 1 <= col <= 6):
                    print("Coordinates should be from 1 to 6!")
                    continue
                if player.opponent.player_field[row - 1, col - 1] in ['X', '*', "■"]:
                    print('This cell is already shot! Choose another one!')
                    continue
                return ShotCoordinates(row - 1, col - 1)
            except ValueError:
                print("You should enter 2 numbers!")

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
