#!/usr/bin/python3
"""
This module defines a Square class that defines a square and includes
functionality for setting size, position, printing the square, and
printing the square object directly.
"""


class Square:
    """
    Class Square that defines a square.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the '#' character according to the position.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Print the vertical offset using the position's second value
        [print("") for _ in range(self.__position[1])]

        # Print each row of the square
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Define the string representation of the square for printing.

        Returns:
            str: A string representation of the square using the '#' character.
        """
        if self.__size == 0:
            return ""

        result = []
        # Add the vertical offset (position[1] new lines)
        result.append("\n" * self.__position[1])

        # Construct the square line by line with the appropriate spaces and '#'
        for i in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
            if i < self.__size - 1:
                result.append("\n")

        return "".join(result)
