from battleship import Battleship


game = Battleship()
user_player, ai_player = game.create_players()

player_to_move = user_player
game.greet()
game.draw_fields(user_player)

while True:
    print(f"\n'{player_to_move.name}' moves")
    coordinates = game.get_new_coordinates(player_to_move)
    shot_result = game.make_shot(coordinates, player_to_move)
    game.draw_fields(user_player)
    status = game.get_game_status(user_player, ai_player)
    if status != 'Game not finished':
        print(status)
        break
    if not shot_result:  # shot_result is True (DAMAGE, no player change) or False (OVERSHOT, then change player)
        player_to_move = player_to_move.opponent
