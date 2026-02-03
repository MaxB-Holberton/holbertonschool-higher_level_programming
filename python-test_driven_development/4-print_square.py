#!/usr/bin/python3
"""
Prints a square based on the input size
"""
def print_square(size):
    """
    Prints a square based on the input size

    Arguments:
        size (int): the size of the square
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()
