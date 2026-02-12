#!/usr/bin/env python3
"""
    Module for showcasing class inheritence and overriding
"""


class Fish:
    """
        The fish class
    """
    def swim(self):
        """
            The fish swim method
        """
        print("The fish is swimming")
    def habitat(self):
        """
            The fish habitat method
        """
        print("The fish lives in water")

class Bird:
    """
        The bird class
    """
    def fly(self):
        """
            The bird fly method
        """
        print("The bird is flying")
    def habitat(self):
        """
            The bird habitat method
        """
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """
        The flying fish class
    """
    def fly(self):
        """
            The flying fish fly method
        """
        print("The flying fish is soaring!")
    def swim(self):
        """
            The flying fish fly method
        """
        print("The flying fish is swimming!")
    def habitat(self):
        """
            The flying fish habitat method
        """
        print("The flying fish lives both in water and the sky!")

