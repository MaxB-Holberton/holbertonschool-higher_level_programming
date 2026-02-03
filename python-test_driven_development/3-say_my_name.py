#!/usr/bin/python3
"""
    A module to print the first and last name
"""
def say_my_name(first_name, last_name=""):
    """
    say my name - prints the first and last name

    Arguments:
        first_name (str): the first name
        last_name (str): the last name
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")

    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
