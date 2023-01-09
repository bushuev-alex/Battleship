from battleship import Battleship


my_game = Battleship("USER", "AI_player")
my_game.greet()
my_game.create_game_fields()
my_game.ai_field()
my_game.draw_ai_field()

while True:
