class LabyrinthTile:
    """ 
    defines from which directions the labyrinth tile is accessible
    """

    def __init__(self, left_access: bool, top_access: bool, right_access: bool, bottom_access: bool):
        """
        Creates a labyrinth tile and defines from which direction it is accessible

        Args:
            left_access: defines if the tile can be accessed from the left
            top_access: defines if the tile can be accessed from the top
            right_access: defines if the tile can be accessed from the right
            bottom_access: defines if the tile can be accessed from the bottom
        """

        self.left_accessible = left_access
        self.top_accessible = top_access
        self.right_accessible = right_access
        self.bottom_accessible = bottom_access

    def __eq__(self, other):
        if not isinstance(other, LabyrinthTile):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.left_accessible == other.left_accessible and self.top_accessible == other.top_accessible and self.right_accessible == other.right_accessible and self.bottom_accessible == other.bottom_accessible
