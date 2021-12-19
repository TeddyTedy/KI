class Position2D:
    """
    defines the position of an object in a two-dimensional grid
    """

    def __init__(self, column: int, row: int):
        """
        stores position of an object in a two-dimensional grid

        Args:
            column: column respectively x-axis value in a two-dimensional grid
            row: row respectively y-axis value in a two-dimensional grid
        """
        self.column: int = column
        self.row: int = row

    def __eq__(self, other):
        if not isinstance(other, Position2D):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.column == other.column and self.row == other.row

    def __hash__(self):
        """
        calculates hash value for object instance, for example needed to be able to use sets of the class type

        Returns: hash value of object instance
        """
        return hash(self.row) + hash(self.column)
