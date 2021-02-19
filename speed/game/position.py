class Position():
    """
    Represents a position/distance from the origin (0, 0)
    The origin is at the top left corner of the screen
    The y position is measured vertically from the origin
    The x position is measured horizontally from the origin

    Stereotype:
        Information Holder

    Attributes:
        _x (int): the horizontal distance
        -Y (int): the vertical distance

    """

    def __init__(self, x, y):
        """
        The class constructor.

        Args:
            self (Position): An instance of Position
            x (integer): horizontal distance from origin
            y (integer): vertical distance from origin
        """
        self._x = x
        self._y = y

    def get_x(self):
        """
        Gets the horizontal distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """
        Gets the vertical distance.
        
        Args:
            self (Point): An instance of Point.
            
        Returns:
            integer: The vertical distance.
        """
        return self._y