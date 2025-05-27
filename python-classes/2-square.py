#!/usr/bin/python3
<<<<<<< HEAD
"""
2-square.py - This module defines a Square class with size validation.
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size=0):
        """
        Initialize the square with a given size.

        Args:
        
=======
"""Module that defines a Square classe"""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Initialize square with given size
        Args:
            size: size of the square
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
