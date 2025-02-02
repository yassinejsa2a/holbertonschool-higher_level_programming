#!/usr/bin/python3
"""Module that defines a Square classe Module that defines a Square classe""""


class Square:
    """Class that defines a square Class that defines a square"""
    def __init__(self, size):
        """Initializes the data."""
        self.__size = size
 	if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
