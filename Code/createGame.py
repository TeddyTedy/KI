import json
from typing import List, Dict

from AStar import AStar
from Position2D import Position2D
from Labyrinth import Labyrinth
from LabyrinthTile import LabyrinthTile

LABYRINTH_FILE_DICTIONARY: Dict = {
    0: LabyrinthTile(False, False, True, True),
    1: LabyrinthTile(True, False, False, True),
    2: LabyrinthTile(False, True, True, False),
    3: LabyrinthTile(True, True, False, False),
    4: LabyrinthTile(True, False, True, True),
    5: LabyrinthTile(True, True, False, True),
    6: LabyrinthTile(True, True, True, False),
    7: LabyrinthTile(False, True, True, True),
    8: LabyrinthTile(False, True, False, True),
    9: LabyrinthTile(True, False, True, False),
    10: LabyrinthTile(True, True, True, True),
    11: LabyrinthTile(False, False, False, False)
}
"""
Maps LabyrinthTile code to correct LabyrinthTile object
- First Boolean Parameter: Access to the left side of the tile
- Second Boolean Parameter: Access to the top side of the tile
- Third Boolean Parameter: Access to the right side of the tile
- Fourth Boolean Parameter: Access to the bottom side of the tile
For Example if the input code is 0, the Labyrinth tile has paths making it accessible from the top and bottom while it 
has no paths on the left and right sides
"""


def create_game(input_path: str) -> AStar:
    """
    - Reads input data
    - transforms input data
    - creates and returns new A* algorithm

    Args:
        input_path: location of the input file storing the initial game configuration

    Returns: AStar Class instance based upon the game input

    """
    import_data = import_puzzle_as_json(input_path)
    labyrinth: List[List[LabyrinthTile]] = get_labyrinth_by_input(import_data['tiles'])
    free_tile: LabyrinthTile = LABYRINTH_FILE_DICTIONARY[import_data['freeTile']]
    starting_position: Position2D = Position2D(import_data['startingPosition']["column"],
                                               import_data['startingPosition']["row"])
    goal_position: Position2D = Position2D(import_data['goalPosition']["column"], import_data['goalPosition']["row"])
    labyrinth: Labyrinth = Labyrinth(labyrinth, free_tile, starting_position, goal_position, 0, 0)
    return AStar(labyrinth, import_data['rowsWithTileInput']["left"], import_data['rowsWithTileInput']["right"])


def get_labyrinth_by_input(input_list: List[List[int]]) -> List[List[LabyrinthTile]]:
    """
    Transforms the two-dimensional list of labyrinth tile codes into real LabyrinthTile objects,
    using the LABYRINTH_FILE_DICTIONARY dictionary for the mapping

    Args:
        input_list: raw two-dimensional list containing the tile codes

    Returns: two-dimensional List of LabyrinthTile
    """
    labyrinth: List[List[LabyrinthTile]] = []
    for row in input_list:
        row_tiles: List[LabyrinthTile] = []
        for tile in row:
            row_tiles.append(LABYRINTH_FILE_DICTIONARY[tile])
        labyrinth.append(row_tiles)

    return labyrinth


def import_puzzle_as_json(input_path: str):
    """
    Opens the file for the given input path, parses it as a JSON file and returns it

    Args:
        input_path: location of the input file storing the initial game configuration

    Returns: parsed json file as a python Object
    """
    with open(input_path) as file:
        data = json.load(file)
        return data
