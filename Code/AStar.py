from Code.Labyrinth import Labyrinth


class AStar:
    """
    Searches a way to reach the goal tile inside the moving labyrinth using the A* algorithm
    """    
    
    def __init__(self, initial_state: Labyrinth, rows_with_tile_input_left: any, rows_with_tile_input_right: any):
        """
        Used to perform A* algorithm to search a way to reach the goal tile inside the moving labyrinth

        Args:
        - initial_state (Labyrinth): initial state of the Labyrinth before any moves
        - rows_with_tile_input_left (any): array containing all rows that allow inserting the free tile on the left, pushing the tile on the right of the row out, becoming the new free tile
        - rows_with_tile_input_right (any): array containing all rows that allow inserting the free tile on the right, pushing the tile on the left of the row out, becoming the new free tile
    
        Instance Variables:
        - combined_heuristic_cost: sum of distance and approximated distance to the goal
        """

        self.rows_with_tile_input_left = rows_with_tile_input_left
        self.rows_with_tile_input_right = rows_with_tile_input_right
        self.open_states_tile_insert_next = [initial_state]
        self.open_states_player_move_next = []
        self.closed_states = []
        
        self.cost = None
        self.finished = False
    
    def solve(self):
        """
        Tries 
        fddffd
        Returns:
            [type]: [description]
        """
        while ( && )
        
        return self
        