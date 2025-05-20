#!/usr/bin/python3
class Square:
    
    def __init__(self, size=0):
        """Initialize the square with a size."""
        self.__size = size
        
        @property
    def size(self):
        """Get the size of the square."""
        return self.__size
        
    @size.setter
    def size(self, size):
       if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
    