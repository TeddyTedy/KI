import json
from Labyrinth import Labyrinth
from LabyrinthTile import LabyrinthTile

LABYRINTH_FILE_DICTIONARY = {
    "0": LabyrinthTile(False, False, True, True),
    "1": LabyrinthTile(True, False, False, True),
    "2": LabyrinthTile(False, True, True, False),
    "3": LabyrinthTile(True, True, False, False),
    "4": LabyrinthTile(True, False, True, True),
    "5": LabyrinthTile(True, True, False, True),
    "6": LabyrinthTile(True, True, True, False),
    "7": LabyrinthTile(False, True, True, True),
    "8": LabyrinthTile(False, True, False, True),
    "9": LabyrinthTile(True, False, True, False),
    "10": LabyrinthTile(True, True, True, True),
    "11": LabyrinthTile(False, False, False, False)
}
"""
Maps LabyrinthTile code to correct LabyrinthTile object
- First Boolean Parameter: Access to the left side of the tile
- Second Boolean Parameter: Access to the top side of the tile
- Third Boolean Parameter: Access to the right side of the tile
- Fourth Boolean Parameter: Access to the bottom side of the tile
For Example if the input code is 0, the Labyrinth tile has paths making it accessible from the top and bottom while it has no paths on the left and right sides
"""
 
def create_game(input_path: str):
    """
    - Reads input data
    - creates initial labyrinth
    - creates and returns new Game
    """
    
    import_data = import_puzzle_as_json(input_path)
    labyrinth = Labyrinth(import_data['tiles'], import_data['freeTile'], import_data['startingPosition']["row"], import_data['startingPosition']["column"], import_data['goalPosition']["row"], import_data['goalPosition']["column"], 0 )
    
    print(labyrinth)
    
   
def import_puzzle_as_json(input_path: str):
    """
    Opens the file for the given input path
    parses it as a JSON file and returns it
    """ 
    
    with open(input_path) as file:
        data = json.load(file)
        return data    

    

