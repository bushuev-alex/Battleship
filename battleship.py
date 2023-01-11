from field import Field
from gamers import Gamer, UserGamer, AIGamer
from game_dataclasses import ShotCoordinates
from exceptions import *


class Battleship:

    def __init__(self, player: str, opponent: str):
        self.players = {player: None, opponent: None}
        self.player_to_move: Gamer = None

    def set_player_to_move(self, player: Gamer):
        self.player_to_move = player

    def create_players(self) -> tuple[Gamer, Gamer]:
        # create field objects:
        user_field = Field()
        ai_field = Field()
        # create players
        user_player = UserGamer(user_field, ai_field)
        ai_player = AIGamer(user_field, ai_field)

        self.players["USER"] = user_player
        self.players["AI"] = ai_player
        return user_player, ai_player

    def greet(self) -> None:
        print("\n-----------------")
        print("  Greeting you   ")
        print("     in game     ")
        print("   Battleship    ")
        print("-----------------")
        print("input format: x y")
        print("  x - row number ")
        print("  y - col number ")
        print("-----------------\n")

    def get_opponent(self, player: Gamer) -> Gamer:
        return self.players["USER"] if player.name == "AI" else self.players["AI"]

    def draw_fields(self, player: Gamer) -> None:
        opponent = self.get_opponent(player)
        print(f"\n  {player.name} Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------')
        for n, row in enumerate(player.player_field):
            print(n + 1, '|', *row, '|')
        print('  ---------------')

        print(f"\n  {opponent.name} Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------')
        for n, row in enumerate(opponent.hiding_field):
            print(n + 1, '|', *row, '|')
        print('  ---------------')


    def draw_fields_(self, player: Gamer) -> None:
        opponent = self.get_opponent(player)

        print(f"\n     {player.name} Field", ' ', ' ', ' ', ' ', f"   {opponent.name} Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6', ' ', ' ', ' ', ' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------', ' ', ' ', '  ---------------')
        for n, rows in enumerate(zip(player.player_field, opponent.hiding_field)):
            print(n + 1, '|', *rows[0], '|', ' ', ' ', n + 1, '|', *rows[1], '|')
        print('  ---------------', ' ', ' ', '  ---------------')

    def get_new_coordinates(self, player: Gamer) -> ShotCoordinates:
        while True:
            try:
                row, col = player.ask_coordinates()

                if not (1 <= row <= 6 and 1 <= col <= 6):
                    print("Coordinates should be from 1 to 6!")
                    continue
                if player.opponent_field[row - 1, col - 1] in ['X', '*', "■"]:
                    print('This cell is already shot! Choose another one!')
                    continue
                return ShotCoordinates(row - 1, col - 1)
            except ValueError:
                print("You should enter 2 numbers!")

    def check_ship_is_live(self, coordinates: ShotCoordinates, opponent: Gamer) -> None:
        row = coordinates.row
        col = coordinates.col
        for ship in opponent.ships:
            # find right ship:
            condition = (row in range(ship.coordinates.row_start, ship.coordinates.row_end + 1) and
                         (col in range(ship.coordinates.col_start, ship.coordinates.col_end + 1)))
            if not condition:
                continue
            ship_dots = ship.get_dots(opponent.player_field)
            if "O" not in ship_dots:
                opponent.player_field[ship.coordinates.row_start:ship.coordinates.row_end + 1,
                                      ship.coordinates.col_start:ship.coordinates.col_end + 1] = "■"
                opponent.hiding_field[ship.coordinates.row_start:ship.coordinates.row_end + 1,
                                      ship.coordinates.col_start:ship.coordinates.col_end + 1] = "■"
                ship.is_live = False
                print("THE SHIP IS KILLED!")
                break

    def make_move(self, coordinates: ShotCoordinates, player: Gamer) -> None:
        row = coordinates.row
        col = coordinates.col
        opponent = self.get_opponent(player)
        if opponent.player_field[row, col] == "O":
            opponent.player_field[row, col] = "X"
            opponent.hiding_field[row, col] = "X"
            print("THE SHIP IS DAMAGED")
            self.check_ship_is_live(coordinates, opponent)
        else:
            opponent.player_field[row, col] = "*"
            opponent.hiding_field[row, col] = "*"
            print("OVERSHOT!")

    def get_game_status(self, user_player: Gamer, ai_player: Gamer) -> str:
        if all(map(lambda x: not x, [ship.is_live for ship in user_player.ships])):
            return "AI WINS!"
        if all(map(lambda x: not x, [ship.is_live for ship in ai_player.ships])):
            return "USER WINS!"
        return "Game not finished"

    def change_player(self):
        self.player_to_move = self.players["USER"] if self.player_to_move.name == "AI" else self.players["AI"]


if __name__ == "__main__":
    game = Battleship("user", "ai_player")
    # game.create_fields()
    # game.draw_fields(game.)
    # game.draw_ai_field()
