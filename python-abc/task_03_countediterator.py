#!/usr/bin/env python3
"""
    Module for the counted iterator class
"""


class CountedIterator:
    """
        Initializes the CountedIterator class
    """
    def __init__(self, i):
        """
            Initializes the class
        """
        self.i = iter(i)
        self.count = 0

    def __next__(self):
        """
            overrides the next method
        """
        try:
            i = next(self.i)
            self.count += 1
            return i
        except StopIteration:
            raise StopIteration

    def get_count(self):
        """
            The count getter
        """
        return self.count
