from battleship import Battleship


my_game = Battleship("USER", "AI")
user_player, ai_player = my_game.create_players()
my_game.set_player_to_move(user_player)

my_game.greet()
my_game.draw_fields(my_game.player_to_move)

while True:
    print(f"\n'{my_game.player_to_move}' moves")
    coordinates = my_game.get_new_coordinates(my_game.player_to_move)
    my_game.make_move(coordinates, my_game.player_to_move)
    my_game.draw_fields(my_game.player_to_move)

    status = my_game.get_game_status(user_player, ai_player)
    if status != 'Game not finished':
        print(status)
        break
    my_game.change_player()
