#!/usr/bin/python3
"""
    A module to add 2 ints together
"""

def convert_float(val):
    """
        convert floats to ints

        Args:
            num: float to cast

        Returns:
            int: the converted number
    """
    if type(val) is float:
        return(int(val))
    return(val)

def add_integer(a, b=98):
    """
    add_integers - does the addition of the ints
    Args:
        a: int or float
        b: int or float

    Returns:
        int: the result of the addition
    """

    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")

    return(convert_float(a) + convert_float(b))
