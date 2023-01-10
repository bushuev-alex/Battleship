from battleship import Battleship


my_game = Battleship("USER", "AI")
user_field, ai_field = my_game.create_fields()
user_player, ai_player = my_game.create_players(user_field, ai_field)

my_game.greet()
my_game.set_player_to_move("USER")
my_game.draw_fields(my_game.player_to_move)

while True:
    print(f"\n'{my_game.player_to_move}' moves")
    coordinates = my_game.get_new_coordinates(my_game.player_to_move)
    my_game.make_move(coordinates, my_game.player_to_move)

    my_game.draw_fields(my_game.player_to_move)
    #field_lines = my_game.get_field_lines(my_game.field)
    #result = my_game.get_game_result(field_lines)
    #if result != 'Game not finished':
#        print(result)
        #break
    my_game.change_player()
