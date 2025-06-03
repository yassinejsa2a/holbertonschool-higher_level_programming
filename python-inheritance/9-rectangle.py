#!/usr/bin/python3



class BaseGeometry:
    """Base class for geometry operations"""

    def area(self):
        """Raises an Exception because area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height
    def __str__(self):
        """Returns a string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
    