import copy

from Position2D import Position2D
from LabyrinthTile import LabyrinthTile
from typing import List, Set


class Labyrinth:
    """
    Stores a specific configuration of the labyrinth
    """

    def __init__(self, labyrinth_tiles: List[List[LabyrinthTile]], free_tile: LabyrinthTile,
                 player_position: Position2D, goal_position: Position2D, distance: int):
        """
        Creates a Labyrinth object which stores the new_state of the labyrinth

        Args:
            labyrinth_tiles: Array containing all tiles of the labyrinth
            free_tile: Free tile that can be inserted at specific positions of the labyrinth
            player_position: two-dimensional position of the player inside the labyrinth
            goal_position: two-dimensional position of the goal tile inside the labyrinth
            distance: cost needed to reach current new_state

        Instance variables
            goal_reached: boolean, whether the player has reached the goal destination
            combined_heuristic_cost: sum of distance and approximated distance to the goal
            max_row_index: maximum number which can be used to access a specific row of the 
                           two-dimensional labyrinth tiles list without causing an error
            max_column_index: maximum number which can be used to access a specific column of 
                           the two-dimensional labyrinth tiles list without causing an error
        """
        self.labyrinth_tiles: List[List[LabyrinthTile]] = labyrinth_tiles
        self.free_tile: LabyrinthTile = free_tile
        self.player_position: Position2D = player_position
        self.goal_position: Position2D = goal_position
        self.distance: int = distance
        self.goal_reached: bool = self.check_goal_reached()
        self.combined_heuristic_cost: float = self.calculate_combined_heuristic_cost()
        self.max_row_index = len(labyrinth_tiles) - 1
        self.max_column_index = len(labyrinth_tiles[0]) - 1

    def check_goal_reached(self) -> bool:
        """
        Checks if the x,y position of the player match the goal destination. Returns the result

        Returns: True if the player reached the goal destination, otherwise false
        """
        return self.goal_position == self.player_position

    def calculate_combined_heuristic_cost(self) -> float:
        """
        - Approximates the heuristic which at least is the distance + 1 (at least one tile insert is needed)
        - also factors in the amount of tiles that have to be passed at a minimum
        - passing a single tile has an aproximated cost of less than one, because only tile insertions increase cost 
          and multiple tiles can be passed per insertion. (0.3 arbitary number)
        - also rewards being positioned on a tile which has access in the directions towards the goal
        
        Returns: approximated cost for the player to reach the goal destination
        """
        approximated_cost = self.distance + 1 + (0.3 * abs(self.goal_position.column - self.player_position.column) + abs(
            self.goal_position.row - self.player_position.row))
        
        # Rewards great access of the player tile by decreasing cost
        best_tile: LabyrinthTile = LabyrinthTile(False, False, False, False)
        reward_each_side: float = 0.3
        if(self.goal_position.row > self.player_position.row):
            best_tile.bottom_accessible = True
            reward_each_side = reward_each_side * 0.5
        elif(self.goal_position.row < self.player_position.row):
            best_tile.top_accessible = True
            reward_each_side = reward_each_side * 0.5
        if(self.goal_position.column > self.player_position.column):
            best_tile.right_accessible = True
            reward_each_side = reward_each_side * 0.5
        elif(self.goal_position.column < self.player_position.column):
            best_tile.left_accessible = True
            reward_each_side = reward_each_side * 0.5
        
        currentTile: LabyrinthTile = self.get_labyrinth_tile(self.player_position)
        if (best_tile.left_accessible and best_tile.left_accessible == currentTile.left_accessible):
            approximated_cost -= reward_each_side
        if (best_tile.top_accessible and best_tile.top_accessible == currentTile.top_accessible):
            approximated_cost -= reward_each_side
        if (best_tile.right_accessible and best_tile.right_accessible == currentTile.right_accessible):
            approximated_cost -= reward_each_side        
        if (best_tile.bottom_accessible and best_tile.bottom_accessible == currentTile.bottom_accessible):
            approximated_cost -= reward_each_side    

        return approximated_cost

    def insert_free_tile(self, left_rows: List[int], right_rows: List[int]):
        """
        Inserts the free/outside tile in all specified rows. The given parameter specify in which rows the free tile
        can be inserted on the left and right side. Returns the resulting states

        Args:
            left_rows: row indexes which allow a tile insertion on the left side
            right_rows: row indexes which allow a tile insertion on the left side

        Returns: different states after all possible insertions of the free tile
        """
        new_states: List[Labyrinth] = []

        for left_row in left_rows:
            new_player_position: Position2D = copy.deepcopy(self.player_position)
            if (new_player_position.row == left_row):
                if (new_player_position.column == self.max_column_index):
                    new_player_position.column = 0
                else: 
                    new_player_position.column += 1
            new_labyrinth_tiles: List[List[LabyrinthTile]] = self.get_labyrinth_tiles_deep_copy()
            new_free_tile: LabyrinthTile = new_labyrinth_tiles[left_row].pop()
            new_labyrinth_tiles[left_row].insert(0, self.free_tile)
            new_states.append(self.get_state_after_tile_insertion(new_labyrinth_tiles, new_free_tile, new_player_position))

        for right_row in right_rows:
            new_player_position: Position2D = copy.deepcopy(self.player_position)
            if (new_player_position.row == right_row):
                if (new_player_position.column == 0):
                    new_player_position.column = self.max_column_index
                else: 
                    new_player_position.column += -1
            new_labyrinth_tiles: List[List[LabyrinthTile]] = self.get_labyrinth_tiles_deep_copy()
            new_free_tile: LabyrinthTile = new_labyrinth_tiles[right_row].pop(0)
            new_labyrinth_tiles[right_row].append(self.free_tile)
            new_states.append(self.get_state_after_tile_insertion(new_labyrinth_tiles, new_free_tile, new_player_position))

        return new_states

    def get_state_after_tile_insertion(self, labyrinth_tiles: List[List[LabyrinthTile]], free_tile: LabyrinthTile, new_player_position: Position2D):
        """
        Creates a new instance of the Labyrinth class after inserting the free tile into the labyrinth. The changed
        properties are given as parameters. Additionally, increases the distance by 1 (cost of the tile insertion)

        Args:
            labyrinth_tiles: Array containing all tiles of the labyrinth
            free_tile: Free tile that can be inserted at specific positions of the labyrinth

        Returns: new Labyrinth instance after tile insertion
        """
        return Labyrinth(labyrinth_tiles, free_tile, new_player_position, self.goal_position, self.distance + 1)

    def move_player(self):
        """
        Checks to which position the player can legally move and returns an array of labyrinth states, one state
        for each position the player legally is able to reach

        Returns: labyrinth states which the player with different legal positions of the player
        """
        new_positions: Set[Position2D] = {self.player_position}
        new_states: List[Labyrinth] = []
        expand_complete: bool = False

        while expand_complete is False:
            positions_iteration: Set[Position2D] = copy.deepcopy(new_positions)

            for current_position in new_positions:
                current_tile: LabyrinthTile = self.get_labyrinth_tile(current_position)

                # Check if the player can move left
                if current_position.column > 0:
                    left_position: Position2D = Position2D(current_position.column - 1, current_position.row)
                    left_tile: LabyrinthTile = self.get_labyrinth_tile(left_position)
                    if current_tile.left_accessible and left_tile.right_accessible:
                        positions_iteration.add(left_position)

                # check if the player can move upwards
                if current_position.row > 0:
                    upper_position: Position2D = Position2D(current_position.column, current_position.row - 1)
                    upper_tile: LabyrinthTile = self.get_labyrinth_tile(upper_position)
                    if current_tile.top_accessible and upper_tile.bottom_accessible:
                        positions_iteration.add(upper_position)

                # check if the player can move right
                if current_position.column < self.max_column_index:
                    rith_position: Position2D = Position2D(current_position.column + 1, current_position.row)
                    right_tile: LabyrinthTile = self.get_labyrinth_tile(rith_position)
                    if current_tile.right_accessible and right_tile.left_accessible:
                        positions_iteration.add(rith_position)

                # check if the player can move down
                if current_position.row < self.max_row_index:
                    lower_position: Position2D = Position2D(current_position.column, current_position.row + 1)
                    lower_tile: LabyrinthTile = self.get_labyrinth_tile(lower_position)
                    if current_tile.bottom_accessible and lower_tile.top_accessible:
                        positions_iteration.add(lower_position)

            expand_complete = len(positions_iteration) == len(new_positions)
            new_positions = new_positions.union(positions_iteration)

        for new_position in new_positions:
            new_states.append(Labyrinth(self.labyrinth_tiles, self.free_tile, new_position, self.goal_position,
                                        self.distance))

        return new_states

    def get_labyrinth_tile(self, position: Position2D) -> LabyrinthTile:
        """
        Gets a labyrinth tile for the given two-dimensional labyrinth grid position

        Args:
            position: two-dimension position inside the labyrinth of the tile

        Returns: labyrinth tile for the given position
        """
        return self.labyrinth_tiles[position.row][position.column]

    def get_labyrinth_tiles_deep_copy(self):
        new_labyrinth = copy.deepcopy(self.labyrinth_tiles)
        return new_labyrinth

    def __eq__(self, other):
        """
        checks if two Labyrinth are equivalent. Does not cheek for the distance and combined heuristic cost !!!

        Args:
            other: Labyrinth object used for the comparison

        Returns: equivalence of the object, except for the properties distance and combined heuristic cost
        """
        if not isinstance(other, Labyrinth):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.labyrinth_tiles == other.labyrinth_tiles and self.free_tile == other.free_tile and self.player_position == other.player_position and self.goal_position == other.goal_position and self.goal_reached == other.goal_reached
