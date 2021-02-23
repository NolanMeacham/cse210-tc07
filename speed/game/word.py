# import statements here
from random import randint
from game import constants
from game.actor import Actor
from game.position import Position

class Word(Actor):
    """
    Word is a string that users read.
    The responsibility of Word is to keep track of each word, the string, 
    position, velocity, and points that the word is worth.

    Attributes:


    """

    def __init__(self, word):
        """
        Class constructor.
        Calls the super class init function (from Actor)


        Args:
            self (Word): An instance of Word
            word (string): a random word from the word bank
        """
        super().__init__()
        self.set_text(word)
        self.set_position(Position(0, randint(2, constants.MAX_Y-1)))
        self.set_velocity(Position(1, 0))
        # TODO: the score for each word should be based on the length of the word and 
        #       its velocity
        self._points = 0 

    def get_word_points(self):
        """
        """
        return self._points
    def set_word_points(self, guessed_word):
        self._points = len(guessed_word)
    
    def get_word(self):
        word = self.get_text()




        