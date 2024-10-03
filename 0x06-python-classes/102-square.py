#!/usr/bin/python3
"""
This module defines a Square class that defines a square, calculates
the area, and supports comparison between Square instances.
"""


class Square:
    """
    Class Square that defines a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square.

        Args:
            size (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If value is not a number (float or int).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Check if two Square instances are equal based on their area.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Check if two Square instances are not equal based on their area.
        """
        return not self.__eq__(other)

    def __lt__(self, other):
        """
        Check if the current square is smaller than another square based
        on area.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Check if the current square is smaller than or equal to another
        square based on area.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

    def __gt__(self, other):
        """
        Check if the current square is greater than another square
        based on area.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Check if the current square is greater than or equal to another
        square based on area.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False
