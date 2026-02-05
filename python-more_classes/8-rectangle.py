#!/usr/bin/python3

"""
    The module for the rectangle
"""
class Rectangle():
    """
        the rectangle class
    """
    number_of_instances = 0
    print_symbol = '#'

    def area(self):
        """
            Get the area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            Get the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width + self.__height) * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Tests to see which rectangle is biggger
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2


    def __init__(self, width=0, height=0):
        """
            inits the Rectangle class
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
            This method prints the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            print()
            return
        rectangle = ""
        for i in range(self.__height - 1):
            rectangle += (self.__width * str(self.print_symbol)) + '\n'

        rectangle += (self.__width * str(self.print_symbol))
        return rectangle

    def __repr__(self):
        """
            This method returns a string representation
            for the instance
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
            Method that is called when the instance
            is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
            Get the width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
            Get the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
            Sets the height of the rectangle
        """
        if isinstance(val, int) is False:
            raise TypeError("height must be an integer")
        if val < 0:
            raise ValueError("height must be >= 0")

        self.__height = val

    @width.setter
    def width(self, val):
        """
            Sets the width of the rectangle
        """
        if isinstance(val, int) is False:
            raise TypeError("width must be an integer")
        if val < 0:
            raise ValueError("width must be >= 0")

        self.__width = val
