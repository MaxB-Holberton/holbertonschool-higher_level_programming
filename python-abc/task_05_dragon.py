#!/usr/bin/env python3
"""
    The module to show mixins
"""


class SwimMixin:
    """
        The Swim mixin method
    """
    def swim(self):
        """
            The Swim mixin method
        """
        print("The creature swims!")

class FlyMixin:
    """
        The Fly mixin method
    """
    def fly(self):
        """
            The Fly mixin method
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
        The dragon class
    """
    def roar(self):
        """
            The Roar method
        """
        print("The dragon roars!")
