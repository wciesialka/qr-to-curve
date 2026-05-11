class QRImage:

    def __init__(self):
        self.__image = [[]]
        self.__current_line = 0
    
    @property
    def bits(self) -> tuple(tuple(bool)):
        '''
        The QR code's image, with True representing a black square and False 
        representing a white square
        '''
        return tuple(tuple(line) for line in self.__image)
    
    def add(self, bit: bool):
        '''
        Add a new bit to the image.

        :param bit: The bit. True for a black square, False for a white square.
        :type bit: bool
        :raises TypeError: bit is not type bool.
        '''
        if not isinstance(bit, bool):
            raise TypeError(f"bit must be type bool, not {type(bit)}")
        self.__image[self.__current_line].append(state)
    
    def new_line(self):
        '''
        Add a new line to the image.
        '''
        self.__current_line += 1