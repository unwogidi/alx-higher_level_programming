#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute 'size'
and a public method to calculate the area of the square.
"""


class Square:
    """
    Class Square that defines a square.

    Attributes:
        __size (int): Size of the square (private).
    """

    def __init__(self, size=0):
        """

        Initialize a new Square instance.

        Args:
            size (int): Size of the square, default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.__size ** 2
