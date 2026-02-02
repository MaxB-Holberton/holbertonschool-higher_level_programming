#!/usr/bin/python3

class Square:
	"""Class Square
	Handles methods involving a square
	"""
	def __init__(self, size=0):
		"""Function __Init
		This function initializes the size of the square

		Attributes:
			size (int): The size of the square

		Raises:
			TypeError: if size is not an int
			ValueError: if size is less than 0
		"""
		if isinstance(size, int) is False:
			raise TypeError("Size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size

	@property
	def size(self):
		"""Getter for Size
		Gets the size for the square
		"""
		return self.__size

	@size.setter
	def size(self, size):
		"""Setter for Size
		Sets the size for the square

		Attributes:
			size (int): The size of the square

		Raises:
			TypeError: if size is not an int
			ValueError: if size is less than 0
		"""
		if isinstance(size, int) is False:
			raise TypeError("Size must be an integer")
		elif size < 0:
			raise ValueError("size must be >= 0")
		else:
			self.__size = size

	def area(self):
		"""Function area
		This function returns the area of the square
		"""
		return self.__size ** 2

	def my_print(self):
		"""Function my_print
		This function prints the entire square size
		to the terminal line with #
		"""
		for i in range(self.__size):
			for j in range(self.__size):
				print("#",end="")

			print()
