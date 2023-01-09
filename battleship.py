from ship import Ship
from field import Field
from gamers import UserGamer, AIGamer


class Battleship:

    def __init__(self, first_player: str, second_player: str):
        self.user_player = UserGamer()
        self.ai_gamer = AIGamer()
        self.user_field = None
        self.ai_field = None

    def create_game_fields(self):
        self.user_player.generate_ships()
        self.ai_gamer.generate_ships()

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

    def draw_fields(self, gamer) -> None:
        print(f"\n    {gamer.user_field} Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------')
        for n, row in enumerate(gamer.field):
            print(n + 1, '|', *row, '|')
        print('  ---------------')

        print(f"\n    {gamer.ai_field} Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------')
        for n, row in enumerate(gamer.field):
            print(n + 1, '|', *row, '|')
        print('  ---------------')


if __name__ == "__main__":
    game = Battleship()
    game.create_game_fields()
    game.draw_fields(game.)
    #game.draw_ai_field()
