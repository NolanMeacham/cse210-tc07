# import statements here
from game.actor import Actor
from game.position import Position

class Score(Actor):
    """

    """

    def __init__(self):
        """
        Class constructor.

        """
        super().__init__()
        self._score = 0
