#!/usr/bin/python3
"""
This module defines a Node class and a SinglyLinkedList class for a sorted
singly linked list.
"""


class Node:
    """
    Class Node that defines a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node or None): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node or None): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Retrieve the data of the node.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The new data for the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Retrieve the next node in the list.

        Returns:
            Node or None: The next node in the list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the list.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class SinglyLinkedList that defines a sorted singly linked list.

    Attributes:
        __head (Node or None): The head of the linked list.
    """

    def __init__(self):
        """Initialize an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """
        Define the string representation of the linked list.

        Returns:
            str: A string representation of the linked list with one data
            per line.
        """
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Insert a new Node with the given value in the correct sorted position.

        Args:
            value (int): The value to insert in the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            # Insert at the beginning
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Find the proper position for the new node
            current = self.__head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
