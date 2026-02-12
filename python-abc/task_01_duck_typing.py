#!/usr/bin/env python3
from abc import ABC, abstractmethod
from math import pi

"""
    Create an abstract Shape method
"""


class Shape(ABC):
    """
        The shape interface class
    """
    @abstractmethod
    def area():
        """
            The area abstract method
        """
        pass

    @abstractmethod
    def perimeter():
        """
            The perimeter abstract method
        """
        pass


class Circle(Shape):
    """
        The circle class
    """
    def __init__(self, radius):
        """
            Initializes the Circle class
        """
        self.__radius = radius

    def area(self):
        """
            Initializes the area method
        """
        return pi * self.__radius ** 2

    def perimeter(self):
        """
            Initializes the perimeter method
        """
        return 2 * pi * self.__radius


class Rectangle(Shape):
    """
        Initializes the Rectangle class
    """
    def __init__(self, width, height):
        """
            Initializes the Rectangle class
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
            Initializes the area method
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Initializes the perimeter method
        """
        return 2 * (self.__width + self.__height)


def shape_info(item):
    """
        shape_info function
    """
    print("Area: {}".format(item.area()))
    print("Perimeter: {}".format(item.perimeter()))
