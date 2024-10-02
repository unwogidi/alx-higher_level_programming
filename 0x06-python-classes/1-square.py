#!/usr/bin/python3
"""
This module defines a square based on empty module
"""

class Square:
    """
    This class defines a square by its size.

    Attributes:
    __size (int): The size of the square, kept private to control access.
    """
    def __init__(self, size):
        """
        Initializes the square with a specific size.

        Args:
        size (int): The size of the square.
        """
        self.__size = size
