#!/usr/bin/python3
<<<<<<< HEAD
"""
This module defines a Rectangle class.
The Rectangle class has two attributes: width and height.
It also has a method to calculate the area of the rectangle.
"""
class Rectangle:
    """
    A class that defines a rectangle by its width and height.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
=======
"""Module that defines a Rectangle class"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize rectangle with given width and height
        Args:
            width: width of the rectangle
            height: height of the rectangle
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
        """
        self.width = width
        self.height = height

    @property
    def width(self):
<<<<<<< HEAD
        """Get the width of the rectangle."""
=======
        """Retrieve width of the rectangle"""
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        """Set the width of the rectangle."""
        if not isinstance(value, int):
=======
        """Set the width of the rectangle"""
        if type(value) is not int:
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """Get the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
=======
        """Retrieve height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) is not int:
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
<<<<<<< HEAD

        
=======
>>>>>>> 5260abd10151aa04c170d5ce7526638bf0ff74d3
