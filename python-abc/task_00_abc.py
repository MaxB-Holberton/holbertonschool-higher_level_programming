#!/usr/bin/env python3
from abc import ABC, abstractmethod
"""
    A module for the animal class and animal subclasses
"""


class Animal(ABC):
    """
        The animal class
    """
    @abstractmethod
    def sound(self):
        """
        The sound method for the animal
        """
        pass


class Dog(Animal):
    """
        The Dog animal class
    """
    def sound(self):
        """
        The sound method for the animal
        """
        return "Bark"


class Cat(Animal):
    """
        The Cat animal class
    """
    def sound(self):
        """
        The sound method for the animal
        """
        return "Meow"
