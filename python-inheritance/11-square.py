#!/usr/bin/python3



class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes the square with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
        
    def __str__(self):
        """Returns a string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"
