from ship import Ship
from field import Field
from gamers import Gamer, UserGamer, AIGamer
from game_dataclasses import ShotCoordinates
from exceptions import *


class Battleship:

    def __init__(self, first_player: str, second_player: str):
        self.players = {first_player: None, second_player: None}
        self.player_to_move = None

    def set_player_to_move(self, player):
        self.player_to_move = player

    def create_fields(self) -> tuple[Field, Field]:
        # create USER player field
        user_field_obj = Field()
        user_field_obj.generate_ships()
        # create AI player field
        ai_field_obj = Field()
        ai_field_obj.generate_ships()
        return user_field_obj, ai_field_obj

    def create_players(self, user_field_obj: Field, ai_field_obj: Field) -> tuple[UserGamer, AIGamer]:
        # create players
        user_player = UserGamer(user_field_obj, ai_field_obj)
        ai_player = AIGamer(user_field_obj, ai_field_obj)
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

    def get_opponent(self, player: str) -> str:
        players = ["USER", "AI"]
        players.remove(player)
        return players[0]

    def draw_fields(self, player: str) -> None:
        player_ = self.players.get(player)
        print(f"\n  {player} Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------')
        field = player_.player_field
        for n, row in enumerate(field):
            print(n + 1, '|', *row, '|')
        print('  ---------------')

        opponent = self.get_opponent(player)
        opponent_ = self.players.get(opponent)
        print(f"\n  {opponent} Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------')
        field = opponent_.hiding_field
        for n, row in enumerate(field):
            print(n + 1, '|', *row, '|')
        print('  ---------------')

    def draw_fields_(self, player: str) -> None:
        player_ = self.players.get(player)
        opponent = self.get_opponent(player)
        opponent_ = self.players.get(opponent)

        print(f"\n     {player} Field", ' ', ' ', ' ', ' ', f"   {opponent} Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6', ' ', ' ', ' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------', ' ', ' ', '  ---------------')
        field = player_.player_field
        opponent_field = opponent_.hiding_field
        for n, rows in enumerate(zip(field, opponent_field)):
            print(n + 1, '|', *rows[0], '|', ' ', ' ', n + 1, '|', *rows[1], '|')
        print('  ---------------', ' ', ' ', '  ---------------')

    def get_new_coordinates(self, player: str) -> ShotCoordinates:
        player_: Gamer = self.players.get(player)
        while True:
            try:
                row, col = player_.ask_coordinates()

                if not (1 <= row <= 6 and 1 <= col <= 6):
                    print("Coordinates should be from 1 to 6!")

                    continue
                if player_.opponent_field[row - 1, col - 1] in ['X', '*', "■"]:
                    print('This cell is already shot! Choose another one!')
                    continue
                return ShotCoordinates(row - 1, col - 1)
            except ValueError:
                print("You should enter 2 numbers!")

    def check_ship_is_live(self, coordinates: ShotCoordinates, opponent: Gamer) -> bool:
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

    def make_move(self, coordinates: ShotCoordinates, player: str):
        row = coordinates.row
        col = coordinates.col
        opponent: Gamer = self.players.get(self.get_opponent(player))
        if opponent.player_field[row, col] == "O":
            opponent.player_field[row, col] = "X"
            opponent.hiding_field[row, col] = "X"
            print("THE SHIP IS DAMAGED")
            self.check_ship_is_live(coordinates, opponent)
        else:
            opponent.player_field[row, col] = "*"
            opponent.hiding_field[row, col] = "*"
            print("OVERSHOT.")

    def get_game_status(self, user_player: Gamer, ai_player: Gamer) -> str:
        if all(map(lambda x: not x, [ship.is_live for ship in user_player.ships])):
            return "AI WINS!"
        if all(map(lambda x: not x, [ship.is_live for ship in ai_player.ships])):
            return "USER WINS!"
        return "Game not finished"

    def change_player(self):
        self.player_to_move = "USER" if self.player_to_move == "AI" else "AI"


if __name__ == "__main__":
    game = Battleship("user", "ai_player")
    game.create_fields()
    # game.draw_fields(game.)
    # game.draw_ai_field()
