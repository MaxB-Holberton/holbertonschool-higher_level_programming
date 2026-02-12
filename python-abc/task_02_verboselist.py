#!/usr/bin/env python3
"""
    Initializes the Circle class
"""


class VerboseList(list):
    """
        Initializes the verboselist class
    """
    def append(self, item):
        """
            the append override methods
        """
        print(f"Added {[item]} to the list.")
        super().append(item)

    def extend(self, item):
        """
            the extend override methods
        """
        print(f"Extended the list with {[len(item)]} items.")
        super().extend(item)

    def remove(self, item):
        """
            the remove override methods
        """
        print(f"Removed {[item]} from the list.")
        super().remove(item)

    def pop(self, item=None):
        """
            the pop override methods
        """
        if item is None:
            popped = super().pop()
            print(f"Popped {[popped]} from the list.")
        else:
            print(f"Popped {[item]} from the list.")
            super().pop(item)
