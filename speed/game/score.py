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

        self.set_text(f"Score : {self._score}")
    def get_score(self):
        return self._score
    def set_score(self, points):
        self._score += points
