from typing import List, Set
from Labyrinth import Labyrinth
from LabyrinthTile import LabyrinthTile
from Position2D import Position2D
from operator import eq

def sort_by_combined_heuristic_cost(e: Labyrinth):
    return e.combined_heuristic_cost

class AStar:
    """
    Searches a way to reach the goal tile inside the moving labyrinth using the A* algorithm
    """

    def __init__(self, initial_state: Labyrinth):
        self.open_states: List[Labyrinth] = [initial_state]

    def compare(self, e: Labyrinth):
        return e.combined_heuristic_cost   
    
    def compareStatic(e: Labyrinth):
        return e.combined_heuristic_cost
           
    def addState(self, state):
        self.open_states.append(state)
        print(len(self.open_states))
        self.open_states.sort(reverse=True, key=sort_by_combined_heuristic_cost)
        
    def compare(sel)
        
tile = LabyrinthTile(False, False, False, False)
labyrinth = [[tile, tile, tile], [tile, tile, tile], [tile, tile, tile]]
position1 = Position2D(0, 0)
position2 = Position2D(1, 1)
position5 = Position2D(1, 2)
position3 = Position2D(2, 2)
position4 = Position2D(0,1)

lab1 = Labyrinth(labyrinth, tile, position2, position1, 0)
lab2 = Labyrinth(labyrinth, tile, position3, position1, 0)
lab3 = Labyrinth(labyrinth, tile, position4, position1, 0)
lab4 = Labyrinth(labyrinth, tile, position5, position1, 0)

astar = AStar(lab1)
astar.addState(lab2)
astar.addState(lab3)
astar.addState(lab4)
astar.open_states.sort(reverse=False, key=sort_by_combined_heuristic_cost)
position_set: Set[Position2D] = {position1}


print(len(position_set))
position_set.add(position2)
print(len(position_set))
position_set.add(position3)
print(len(position_set))

print("End Sts")
tile1 = LabyrinthTile(False, False, True, True)
tile2 = LabyrinthTile(False, False, True, True)
tile3 = LabyrinthTile(False, False, True, True)
tile4 = LabyrinthTile(False, False, True, True)
tile5 = LabyrinthTile(False, False, False, True)
tile6 = LabyrinthTile(False, False, True, True)
tile7 = LabyrinthTile(False, False, True, True)
tile8 = LabyrinthTile(False, True, True, True)
tile9 = LabyrinthTile(False, False, True, True)

pile1 = LabyrinthTile(False, False, True, True)
pile2 = LabyrinthTile(True, True, True, True)
pile3 = LabyrinthTile(False, False, True, True)
pile4 = LabyrinthTile(False, False, True, True)
pile5 = LabyrinthTile(False, False, False, True)
pile6 = LabyrinthTile(False, False, True, True)
pile7 = LabyrinthTile(False, False, True, True)
pile8 = LabyrinthTile(False, True, True, True)
pile9 = LabyrinthTile(False, False, True, True)

labyrinth1 = [[tile1, tile2, tile3], [tile4, tile5, tile6], [tile7, tile8, tile9]]
labyrinth2 = [[pile1, pile2, pile3], [pile4, pile5, pile6]]

print(len(labyrinth2))

print(labyrinth2[0][1] == pile2)

print(labyrinth1 == labyrinth2)

print(len(onedimensional))

onedimensional = [s for s in onedimensional if s != pile8]

print(len(onedimensional))



def myFunc(e):
    return e['year']


class LabyrinthTest:
    id: int = 0

    # Creates a Labyrinth Tiles and defines from which direction it is accessible
    def __init__(self, labyrinth_tiles: List[LabyrinthTile], player_row: int, player_column: int, goal_row: int,
                 goal_column: int, distance: int):
        self.id = id
        self.labyrinth_tiles = labyrinth_tiles
        self.player_row = player_row
        self.player_column = player_column
        self.goal_row = goal_row
        self.goal_column = goal_column
        self.distance = distance


cars = [
    {'car': 'Ford', 'year': 2005},
    {'car': 'Mitsubishi', 'year': 2000},
    {'car': 'BMW', 'year': 2019},
    {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)

cars.append({'car': '+=', 'year': 2011})

print(cars)
