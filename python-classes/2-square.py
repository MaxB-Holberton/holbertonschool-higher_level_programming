#!/usr/bin/python3

"""A Module for creating a class called Square"""
class Square:
	"""Class Square
	Stores the size of a square
	"""
	def __init__(self, size=0):
		"""Function __Init
		This function initializes the size of the square

		Attributes:
			size (int): The size of the square
		"""
		if isinstance(size, int) is False:
			raise TypeError("Size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size
