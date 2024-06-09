# Battleship
## Game description
Battleship is a command line interface (CLI) game for two players.\

## How to launch
Proceed to the folder where main.py is located.\
Insert in command line following string with selected players.

#### Example:  
cd `way_to_folder_with_main.py` \
python main.py **--player_lvl**=`user_ai` **--opponent_lvl**=`medium_ai`

When you launch game in CLI, you'll have to specify difficulty level for each of two players. Now three levels of difficulty are available: 
* `user` - have to insert shot coordinates manually
* `easy_ai` - always randomly select coordinates to shot 
* `medium_ai` - randomly select coordinates to shot, but if ship is damaged, next shot is closely to previous one
* ~~`hard_ai`~~ (not realised, coming soon) - randomly select coordinates to shot, but if ship is damaged, next shots will kill them  

So, a pair of gamers looks like:
* `user` - `easy_ai` 
* `easy_ai` - `easy_ai`
* `user` - `medium_ai`
* `medium_ai` - `medium_ai`
* `medium_ai` - `easy_ai`
* `e.t.c.`

#### Default pair of players is user - medium_ai.

Each player has his own field with ships:
* 1 ship - length 3 
* 2 ships - length 2
* 4 ships - length 1


