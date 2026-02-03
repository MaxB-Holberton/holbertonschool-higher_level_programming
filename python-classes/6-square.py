#!/usr/bin/python3
"""A Module for creating a class called Square"""


class Square:
    """Class Square
    Handles methods involving a square
    """

    def __size_validation(self, size):
        """Function __size_validation
        checks to ensure that the size is valid
        """
        if isinstance(size, int) is False:
            raise TypeError("Size must be an integer")
            return False
        if size < 0:
            raise ValueError("size must be >= 0")
            return False

        return True

    def __position_validation(self, position):
        """Function __position_validation
        checks to ensure that the squqare position is valid
        """
        val = True
        if isinstance(position, tuple) is False:
            val = False
        elif isinstance(position[0], int) is False:
            val = False
        elif isinstance(position[1], int) is False:
            val = False
        elif len(position) > 2:
            val = False
        elif position[0] < 0 or position[1] < 0:
            val = False

        if val is False:
            raise TypeError("position must be a tuple of 2 positive integers")

        return val

    @property
    def size(self):
        """Getter for Size
        Gets the size for the square
        """
        return self.__size

    @property
    def position(self):
        """Getter for position
        Gets the size for the square
        """
        return self.__position

    @position.setter
    def position(self, position):
        """Setter for position
        Sets the size for the position
        """
        if __position_validation(position) is True:
            self.__position = position

    @size.setter
    def size(self, size):
        """Setter for Size
        Sets the size for the square
        """
        if __size_validation(size) is True:
            self.__size = size

    def area(self):
        """Function area
        This function returns the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Function my_print
        This function prints the entire square size
        to the terminal line with #
        """
        if self.size == 0:
            print()
            return

        for k in range(self.position[1]):
            print()
        for i in range(self.__size):
            for line_space in range(self.position[0]):
                print("_", end="")
            for j in range(self.__size):
                print("#", end="")

            print()

    def __init__(self, size=0, position=(0, 0)):
        """Function __Init
        This function initializes the size of the square
        """
        if self.__size_validation(size) is True:
            self.__size = size

        if self.__position_validation(position) is True:
            self.__position = position
