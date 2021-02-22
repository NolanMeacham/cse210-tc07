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
        self._inputted_letter = ''


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

        for i in range(random.randint(1,2)):
            word = Word(self._get_random_word())
            self._current_words.append(word)

        print(len(self._current_words))

    def move_word_list(self, actor_list):
        """
        """
        for actor in actor_list:
            actor.move_next() 

    def setup_game(self):
        pass

         #TODO intialize everything that needs to happen before main game loop
    def _get_inputs(self):
        """

        """
       
        self._inputted_letter = self._input_service.get_letter()
        #The only input that happens is within buffer, so do whatever buffer tells you, haha
        
        pass
    def _do_updates(self):
        """

        """
        if self._inputted_letter == '*':
            self._buffer.reset_buffer()
        else:
            
        self.move_word_list(self._current_words)
        #TODO
        #See if the contents of the buffer is in the screen
            


        #Update Score
        pass

    def _do_outputs(self):
        """
        
        """
        self._output_service.clear_screen()
        
        if len(self._current_words) < 15:
            
            self._make_words()


        self._output_service.draw_actors(self._current_words)

        self._output_service.flush_buffer()
        #TODO
        #Display score

        #Display words at given position

        #Display the buffer text
        pass