from LabyrinthTile import LabyrinthTile

class Labyrinth:
    """
    Stores a specific configuration of the labyrinth

    Args:
    - labyrinth_tiles: Array containing all tiles of the labyrinth
    - free_tile: Free tile that can be inserted at specific postions of the labyrinth 
    - player_row: player position - row respectively x-axis position
    - player_column: player position - column respectively y-axis position
    - goal_row: goal position - row respectively x-axis position
    - goal_column: goal position - column respectively y-axis position
    - distance: cost needed to reach current state
    
    Instance Variables:
    - combined_heuristic_cost: sum of distance and approximated distance to the goal
    """
    
    id: int = 0
       
    # Creates a Labyrinth Tiles and defines from which direction it is accessible
    def __init__(self, labyrinth_tiles, free_tile: LabyrinthTile ,player_row: int, player_column: int, goal_row: int, goal_column: int, distance: int ):
        self.id = id
        self.labyrinth_tiles = labyrinth_tiles 
        self.free_tile = free_tile 
        self.player_row = player_row
        self.player_column = player_column
        self.goal_row = goal_row
        self.goal_column = goal_column
        self.distance = distance
        self.combined_heuristic_cost = None
        self.calculate_combined_heuristic_cost()

    def calculate_combined_heuristic_cost(self):
        """
        - Calculates combined heuristic cost by adding the current distance and an approximated distance to the goal
        - Approximates the distance to the goal by using the minimum number of tiles the player has to pass to reach the goal
        """
        self.combined_heuristic_cost = self.distance + abs(self.goal_column - self.player_column) + abs(self.goal_row - self.player_row)
    
    def insertTiles(self)