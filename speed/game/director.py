from time import sleep
from game import constants

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:

    """
    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._output_service = output_service

        self.keep_playing = True

    def start_game(self):
        """
        """
        pass

    def _get_inputs(self):
        """
        """
        pass

    def _do_updates(self):
        """
        """
        pass

    def _do_outputs(self):
        """
        """
        pass