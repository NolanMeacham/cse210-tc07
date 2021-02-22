
# import statements here
from game.actor import Actor
from game.position import Position

class Buffer(Actor):
    """

    """

    def __init__(self):
        """
        Class constructor.

        """
        super().__init__()
        self._buffer = []        
        self._text_buffer = '-Buffer:{}'
    
    def init_buffer(self):
        for i in range(52):
            self._buffer.append('-')

    def clear_buffer(self):
        pass

    def set_letter(self):
        pass

    def get_buffer(self):
        return self._buffer

    def get_buffer_display(self):
        pass 

# test = Buffer()

# test.init_buffer()

# print(test.get_buffer())