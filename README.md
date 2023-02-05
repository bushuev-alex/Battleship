# Battleship
## Game description
Battleship is a command line interface (CLI) game for two players.\
When you launch game in CLI, you can select two players:
* user - have to insert shot coordinates manually
* easy_ai - always randomly select coordinates to shot 
* medium_ai - randomly select coordinates to shot, but if ship is damaged, next shot is closely to previous one
* hard_ai (not realised functionality, coming soon) - randomly select coordinates to shot, but if ship is damaged, next shots will kill them  

So, a pair of gamers looks like:
* user - easy_ai 
* user - medium_ai 
* medium_ai - hard_ai
* e.t.c.
#### Default pair of players is user - medium_ai.

Each player has his own field with ships:
* 1 ship - with length 3 
* 2 ships - with length 2
* 4 ships - with length 1

## How to launch
Proceed to the folder where main.py is located.\
Insert in command line following string with selected players.

#### Example:  
cd /way_to_folder_with_main.py \
python3 main.py user medium_ai
