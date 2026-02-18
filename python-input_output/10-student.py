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

    def to_json(self, attrs=None):
        """
            returns the entire class to a json string
            or returns specified attributes
        """
        class_dict = self.__dict__
        rtn_dict = dict()

        if type(attrs) is list:
            for i in attrs:
                if type(i) is not str:
                    return class_dict

                if i in class_dict:
                    rtn_dict[i] = class_dict[i]

            return rtn_dict
        return class_dict
