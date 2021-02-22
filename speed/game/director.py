import random
from time import sleep
from game import constants
from game.buffer import Buffer
from game.word import Word
from game.position import Position



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
        self._buffer = Buffer()
        self.word_choice = ''
        self._current_words = []


        self._keep_playing = True

    def start_game(self):
        """

        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_random_word(self):
        
        words = open('speed\game\words.txt').read().splitlines()

        return random.choice(words)

    def _make_words(self):

        for i in range(5):
            word = Word(self._get_random_word())
            self._current_words.append(word)

    def setup_game(self):
        pass

         #TODO intialize everything that needs to happen before main game loop
    def _get_inputs(self):
        """

        """
       
 
        #The only input that happens is within buffer, so do whatever buffer tells you, haha
        
        pass
    def _do_updates(self):
        """

        """
        #TODO
        #See if the contents of the buffer is in the screen
            
        #Move words 

        #Update Score
        pass

    def _do_outputs(self):
        """
        
        """
        self._output_service.clear_screen()
        
        self._make_words()

        self._output_service.draw_actors(self._current_words)

        self._output_service.flush_buffer()
        #TODO
        #Display score

        #Display words at given position

        #Display the buffer text
        pass