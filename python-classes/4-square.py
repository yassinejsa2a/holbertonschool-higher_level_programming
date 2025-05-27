#!/usr/bin/python3
<<<<<<< HEAD
"""
4-square.py - This module defines a Square class with size validation,
getter and setter methods, and a method to calculate the area of the square.
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
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Set the size of the square with validation.

        Args:
            size (int): The new size of the square. Must be an integer >= 0.

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

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.__size = value
        if type(value) is not int:
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
<<<<<<< HEAD
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
=======
        """Returns The area of the square"""
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
        return self.__size ** 2
