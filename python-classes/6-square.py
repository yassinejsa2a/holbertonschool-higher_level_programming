#!/usr/bin/python3
"""Module that defines a Square classe Module that defines a Square classe""""


class Square:
    """Class that defines a square Class that defines a square"""
    def __init__(self, size):
        """Initializes the data."""
        self.__size = size

        @property
        def size(self):
                """Returns the size of the square."""
        return self.__size

         @size.setter
        def size(self, size):
        """Sets the size of the square."""
        if type(size) is not int:
	raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
                """Returns the area of the square"""
        return self.__size ** 2

        def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
