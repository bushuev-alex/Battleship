from battleship import Battleship


my_game = Battleship("USER", "AI")
user_field, ai_field = my_game.create_fields()
user_player, ai_player = my_game.create_players(user_field, ai_field)

my_game.greet()
my_game.set_player_to_move("USER")
my_game.draw_fields_(my_game.player_to_move)

while True:
    print(f"\n'{my_game.player_to_move}' moves")
    coordinates = my_game.get_new_coordinates(my_game.player_to_move)
    my_game.make_move(coordinates, my_game.player_to_move)
    my_game.draw_fields_(my_game.player_to_move)

    status = my_game.get_game_status(user_player, ai_player)
    if status != 'Game not finished':
        print(status)
        break
    my_game.change_player()
