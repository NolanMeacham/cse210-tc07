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
            Begins the game cycle
        """
        self.setup_game()
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_random_word(self):
        """
        This function retrieves a random word from the txt file.
        """
        words = open('speed\game\words.txt').read().splitlines()

        return random.choice(words)

    def _make_words(self):
        """
        This function makes word actors with random words pulled from the txt file.
        """

        for i in range(random.randint(1,2)):
            word = Word(self._get_random_word())
            self._current_words.append(word)
            self._text_words.append(word.get_text())


    def move_word_list(self, actor_list):
        """
        This function takes the list of word actors and moves them all according to their velocity. 
        """
        for actor in actor_list:
            actor.move_next() 

    def setup_game(self):
        """
        Resets the buffer so that it displays correctly at the beginning
        """
        self._buffer.reset_buffer()

    def _get_inputs(self):
        """
        Gets the keystrokes of the player
        """
       
        self._inputted_letter = self._input_service.get_letter()
        
        
        
        
    def _do_updates(self):
        """
        With the keystrokes, this function writes the letters to the buffer,
        checks if the keystrokes match the moving word actors, and moves the
        actors continuely. 
        """
        if self._inputted_letter:
            if self._inputted_letter == '*':
                self._buffer.reset_buffer()
                
            else:
                self._buffer.set_letter(self._inputted_letter)
        
        
        if self._buffer.get_text_buffer() != '':
            buffer = self._buffer.get_text_buffer()
            if 'bombz' in buffer:
                self._score.set_score(random.randint(1000,10000))
                self._score.set_text(f'Score : {self._score.get_score()}')
                self._text_words.clear()
                self._current_words.clear()
            self._text_words
            for i in self._text_words:
                if i in buffer:
                    self._score.set_word_points(i)

                    index = self._text_words.index(i)

                    del self._text_words[index]
                    del self._current_words[index]
                    break

                
        
            

        self.move_word_list(self._current_words)


    def _do_outputs(self):
        """
        This function refreshes the asciimatics screen, and adds more words to the screen 
        if there are less than 15 currently being displayed. It also draws all of the game
        components to the screen. 
        """
        self._output_service.clear_screen()
        
        test = len(self._current_words)
        if len(self._current_words) < 15:
            
            self._make_words()
        

        self._output_service.draw_actor(self._score)
        self._output_service.draw_actors(self._current_words)
        self._output_service.draw_actor(self._buffer)

        self._output_service.flush_buffer()
