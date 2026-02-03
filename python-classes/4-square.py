#!/usr/bin/python3
"""A Module for creating a class called Square"""


class Square:
    """Class Square
    Handles methods involving square
    """
    def __init__(self, size=0):
        """Function __Init
        This function initializes the size of the square
        """
        if isinstance(size, int) is False:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Getter for Size
        Gets the size for the square
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for Size
        Sets the size for the square
        """
        if isinstance(size, int) is False:
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Function area
        This function returns the area of the square
        """
        return self.__size ** 2
