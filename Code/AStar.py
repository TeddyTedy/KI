from typing import List
from Labyrinth import Labyrinth


def sort_by_combined_heuristic_cost(e: Labyrinth) -> bool:
    """
    - Simple function that is needed to sort an array of the type Labyrinth by the combined heuristic cost
    - Cannot be inside the class (Python constraint)

    Args:
        e: Labyrinth object instance to be compared

    Returns: object property used for the comparison
    """
    return e.combined_heuristic_cost


class AStar:
    """
    Searches a way to reach the goal tile inside the moving labyrinth using the A* algorithm
    """

    def __init__(self, initial_state: Labyrinth, rows_with_tile_input_left: List[int],
                 rows_with_tile_input_right: List[int]):
        """
        Used to perform A* algorithm to search a way to reach the goal tile inside the moving labyrinth

        Args:
            initial_state (Labyrinth): initial state of the Labyrinth before any moves
            rows_with_tile_input_left (any): array containing all rows that allow inserting the free tile on the left, pushing the tile on the right of the row out, becoming the new free tile
            rows_with_tile_input_right (any): array containing all rows that allow inserting the free tile on the right, pushing the tile on the left of the row out, becoming the new free tile

        Instance Variables:
            open_states: contains all open states, sorted by the combined heuristic cost
            closed_states: stores all states that already have been
            cost: cost to reach the goal, only set if the algorithm successfully finished
        """
        self.rows_with_tile_input_left: List[int] = rows_with_tile_input_left
        self.rows_with_tile_input_right: List[int] = rows_with_tile_input_right
        self.open_states: List[Labyrinth] = [initial_state]
        self.closed_states: List[Labyrinth] = []
        self.cost: int = None

    def solve(self):

        while len(self.open_states) > 0 and self.cost is None:
            best_state: Labyrinth = self.open_states.pop()
            print("Open states:  %a" % len(self.open_states))
            print("Closed states:  %a" % len(self.closed_states))
            print("Goal reached:  %a" % best_state.goal_reached)
            print("combined heuristic cost:  %a" % best_state.combined_heuristic_cost)
            print("distance:  %a" % best_state.distance)
            print("Player column:  %a" % best_state.player_position.column)
            print("Player row:  %a" % best_state.player_position.row)
            print("-------------------------------------------------")
            states_after_tile_insertion: List[Labyrinth] = best_state.insert_free_tile(self.rows_with_tile_input_left,
                                                                                       self.rows_with_tile_input_right)
            for state_after_tile_insertion in states_after_tile_insertion:
                states_after_moving: List[Labyrinth] = (state_after_tile_insertion.move_player())
                for new_state in states_after_moving:
                    if new_state.goal_reached:
                        self.cost = new_state.distance
                        break
                    else:
                        self.add_state_to_priority_queue(new_state)

            self.closed_states.append(best_state)

        if self.cost:
            print("Using the A* algorithm, the fasted way to reach the goal destination is %a moves" % self.cost)
        else:
            print("The algorithm was unable to to find a solution in which the player is able to reach the goal "
                  "destination inside the moving labyrinth")

    def add_state_to_priority_queue(self, new_state: Labyrinth):
        """
        Updates the list of open states by adding/removing items according to different criteria and reordering
        the list if changes have been made. The criteria are the following
        - a state is similar if the labyrinth tiles, the player and goal position are identical
        - removes a similar state from the priority queue if the given state has a lower combined heuristic cost
        - does not add the given state if the priority queue contains a state with a lower combined heuristic cost
        - does not add the state if it already has been evaluated (contained in closed state)

        Args:
            new_state: new state, to be added to the open state list if it meets the criteria
        """
        similar_closed_states: List[Labyrinth] = [s for s in self.closed_states if s == new_state]

        if len(similar_closed_states) == 0:
            # the new state is not contained inside the closed states list
            similar_open_states: List[Labyrinth] = [s for s in self.open_states if s == new_state]

            if len(similar_open_states) > 0:
                # there is a similar open state to the new state
                similar_states_but_worse_cost: List[Labyrinth] = [s for s in similar_open_states if s.distance > new_state.distance]

                if len(similar_states_but_worse_cost) > 0:
                    # List of open states a state which has a worse cost than the open state
                    worse_state: Labyrinth = similar_states_but_worse_cost.pop()
                    self.open_states = [s for s in self.open_states if s != worse_state and s.distance != worse_state.distance]
                    self.open_states.sort(reverse=True, key=sort_by_combined_heuristic_cost)

            else:
                # there is now open state that is similar to the new state
                self.open_states.append(new_state)
                self.open_states.sort(reverse=True, key=sort_by_combined_heuristic_cost)
