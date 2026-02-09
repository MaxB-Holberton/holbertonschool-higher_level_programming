#!/usr/bin/python3
"""
A module to print a list
"""


class MyList(list):
    """
        a list class for sorting lists
    """
    def print_sorted(self):
        """
            prints a sorted list
        """
        if issubclass(MyList, list):
            print(sorted(self))
