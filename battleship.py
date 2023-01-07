from ship import Ship
from field import Field


class Game:

    def __init__(self):
        self.user_field = Field()
        self.ai_field = Field()

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

    def draw_user_field(self) -> None:
        print("\n    USER Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------')
        for n, row in enumerate(self.user_field.ready_field):
            print(n + 1, '|', *row, '|')
        print('  ---------------')

    def draw_ai_field(self) -> None:
        print("\n     AI Field")
        print(' ', ' ', '1', '2', '3', '4', '5', '6')
        print('  ---------------')
        for n, row in enumerate(self.ai_field):
            print(n + 1, '|', *row, '|')
        print('  ---------------')

