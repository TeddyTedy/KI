class LabyrinthTile:
    """ 
    defines from which directions the labyrinth tile is accessible
    """    

    def __init__(self, left_access: bool, top_access: bool, right_access:bool, bottom_access: bool):
        """
        Creates a Labyrinth Tiles and defines from which direction it is accessible
        """
        self.left_accessible = left_access
        self.top_accessible = top_access
        self.right_accessible = right_access
        self.bottom_accessible = bottom_access
        