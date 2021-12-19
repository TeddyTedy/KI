import createGame
from AStar import AStar

a_star: AStar = createGame.create_game('./input/puzzle.json')
a_star.solve()
a_star.print_result()
