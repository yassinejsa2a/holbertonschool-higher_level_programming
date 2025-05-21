#!/usr/bin/python3
"""
1-square.py - This module defines a Square class with a private size attribute.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private attribute).
    """

    def __init__(self, size):
        """
        Initialize the square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        