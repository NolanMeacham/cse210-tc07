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
            self (Position): An instance of Position.
            
        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """
        Gets the vertical distance.
        
        Args:
            self (Position): An instance of Position.
            
        Returns:
            integer: The vertical distance.
        """
        return self._y
    
    def add(self, other):
        """Gets a new Position that is the sum of this and the given one.

        Args:
            self (Position): An instance of Position.
            other (Position): The Position to add.

        Returns:
            Position: A new Position that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Position(x, y)

    def equals(self, other):
        """Whether or not this Position is equal to the given one.

        Args:
            self (Position): An instance of Position.
            other (Position): The Position to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()
    
    def reverse(self):
        """Gets a new Position that is the reverse of this one.
        
        Args:
            self (Position): An instance of Position.
            
        Returns:
            Position: A new Position that is reversed.
        """
        x = self._x * -1
        y = self._y * -1
        return Position(x, y)