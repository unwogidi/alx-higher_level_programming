#!/usr/bin/python3
"""
This module defines a class Square with private instance attributes 'size' and
'position', getter and setter methods, and methods to calculate the area and
print the square.
"""


class Square:
    """
    Class Square that defines a square.

    Attributes:
        __size (int): Size of the square (private).
        __position (tuple): Position to print the square (private).
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): Size of the square, default is 0.
            position (tuple): Position for the square, default is (0, 0).

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
            value (tuple): A tuple of 2 positive integers.

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
        Print the square with the character '#'.

        If size is 0, print an empty line.
        The square is printed according to the position attribute.
        """
        if self.__size == 0:
            print("")
        else:
            # Print the vertical space (position[1])
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                # Print horizontal spaces and then the square
                print(" " * self.__position[0] + "#" * self.__size)
