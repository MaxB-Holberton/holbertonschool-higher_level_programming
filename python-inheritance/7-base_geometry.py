#!/usr/bin/python3
"""
    Module for BaseGeometry
"""


class BaseGeometry:
    """
        BaseGeometry class
    """
    def area(self):
        """
        Returns an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks for valid input for the base
        """
        if isinstance(name, str) is False:
            raise TypeError("Name must be a string")
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
