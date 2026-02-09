#!/usr/bin/python3
"""
    Module with a class for checking if the object inherits
"""


def inherits_from(obj, a_class):
    """
        function to check object inheritence
    """
    inst = isinstance(obj, a_class)
    sub = issubclass(a_class, obj.__class__)
    if inst and sub is False:
        return True
    return False
