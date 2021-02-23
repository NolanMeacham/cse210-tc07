import random
from time import sleep
from game import constants
from game.buffer import Buffer
from game.word import Word
from game.position import Position
from game.score import Score



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
        self._word = Word('test')
        self._current_words = []
        self._text_words = []
        self._inputted_letter = ''
        self._score = Score()


        self._keep_playing = True

    def start_game(self):
        """

        """
        self.setup_game()
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
            self._text_words.append(word.get_text())


    def move_word_list(self, actor_list):
        """
        """
        for actor in actor_list:
            actor.move_next() 

    def setup_game(self):
        self._buffer.reset_buffer()

         #TODO intialize everything that needs to happen before main game loop
    def _get_inputs(self):
        """

        """
       
        self._inputted_letter = self._input_service.get_letter()
        
        
        
        
    def _do_updates(self):
        """

        """
        if self._inputted_letter:
            if self._inputted_letter == '*':
                self._buffer.reset_buffer()
                
            else:
                self._buffer.set_letter(self._inputted_letter)
        
        
        if self._buffer.get_text_buffer() != '':
            buffer = self._buffer.get_text_buffer()
            self._text_words
            for i in self._text_words:
                if i in buffer:
                    self._word.set_word_points(i)
                    self._score.set_score(self._word.get_word_points())
                    index = self._text_words.index(i)
                    index
                    del self._text_words[index]
                    del self._current_words[index]
                    break

                
        
            

        self.move_word_list(self._current_words)


    def _do_outputs(self):
        """
        
        """
        self._output_service.clear_screen()
        
        test = len(self._current_words)
        if len(self._current_words) < 15:
            
            self._make_words()

        self._output_service.draw_actor(self._score)
        self._output_service.draw_actors(self._current_words)
        self._output_service.draw_actor(self._buffer)

        self._output_service.flush_buffer()

        #Display score

        #Display words at given position

        #Display the buffer text