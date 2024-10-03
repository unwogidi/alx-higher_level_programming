#!/usr/bin/python3
"""
This module defines a class Square with a private instance attribute 'size',
getter and setter methods for manipulating 'size', and methods to calculate
the area and print the square.
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
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the character '#'.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
