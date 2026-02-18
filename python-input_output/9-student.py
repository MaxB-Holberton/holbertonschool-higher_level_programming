#!/usr/bin/python3

"""
    Module for creating a student class
"""


class Student:
    """
        The student class
    """
    def __init__(self, first_name, last_name, age):
        """
            Initializes the class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            returns the entire class to a json string
        """
        return self.__dict__
