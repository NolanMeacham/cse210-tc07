
# import statements here
from game.actor import Actor
from game.position import Position
import numpy as np

class Buffer(Actor):
    """

    """

    def __init__(self):
        """
        Class constructor.

        """
        super().__init__()
        self._buffer = []        
        self._display_buffer = '-Buffer:'
        self._text_buffer = ''
        self.set_position(Position(1, 20))
        self.set_text(self._display_buffer + self._text_buffer) 

    def reset_buffer(self):
        self._buffer = []
        for i in range(52):
            self._buffer.append('-')

    def set_letter(self, letter):
        self._buffer.append(letter)
        # self._buffer = np.roll(self._buffer,-1)
        # self._buffer = np.resize(self._buffer, self._buffer.size - 1)
        # self._buffer= self._buffer.tolist()

    def get_buffer(self):
        return self._buffer

    def set_display_buffer(self):
        self._display_buffer = '-Buffer:'
        for i in self._buffer:
            self._display_buffer += i
    
    def set_text_buffer(self):
        # self._text_buffer = ''
        for i in self._buffer:
            if i == '-':
                pass
            else:
                self._text_buffer += i
    
    def get_text_buffer(self):
        return self._text_buffer

