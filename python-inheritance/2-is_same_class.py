#!/usr/bin/python3
"""
    Module with a class for checking if the obj is the same class
"""


def is_same_class(obj, a_class):
    """
        function for checking if the obj is the same class
    """
    if type(obj) is a_class:
        return True
    return False
