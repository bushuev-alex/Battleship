from battleship import Battleship
import argparse


my_parser = argparse.ArgumentParser()
my_parser.add_argument("-p1", "--player", default="user",
                       help='Select from list [user/easy_ai/medium_ai/hard_ai]')
my_parser.add_argument("-p2", "--opponent", default="medium_ai",
                       help='Select from list [user/easy_ai/medium_ai/hard_ai]')
args = my_parser.parse_args()


game = Battleship(args.player, args.opponent)
player_1, player_2 = game.create_players()

player_to_move = player_1
game.greet()
game.draw_fields(player_1)

while True:
    print(f"\n'{player_to_move.name}' moves")
    coordinates = game.get_new_coordinates(player_to_move)
    shot_result = game.make_shot(coordinates, player_to_move)
    game.draw_fields(player_1)
    status = game.get_game_status(player_1, player_2)
    if status != 'Game not finished':
        print(status)
        break
    if not shot_result:  # shot_result is True (DAMAGE, no player change) or False (OVERSHOT, then change player)
        player_to_move = player_to_move.opponent
