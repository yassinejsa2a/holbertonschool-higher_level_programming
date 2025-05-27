#!/usr/bin/python3
<<<<<<< HEAD
"""
3-square.py - This module defines a Square class with size validation
and a method to calculate the area of the square.
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
            size (int): The size of the square. Must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
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
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
<<<<<<< HEAD
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
    
=======
        """Returns The area of the square"""
        return self.__size ** 2
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
