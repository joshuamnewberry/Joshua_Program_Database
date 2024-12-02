from typing import Any
from node import *

def tuple_conditions(data:tuple[int]) -> None:
    """
    Check tuple[int] of length 2 conditions and raise proper Errors

    Parameters:
    data:tuple[int] the tuple to get checked

    Return:
    None
    
    """
    # If not a tuple
    if type(data) != tuple:
        raise TypeError("Expected type tuple[int]")
    # If not length 2
    if len(data) != 2:
        raise ValueError("Expected length 2 tuple")
    # If values aren't int
    if type(data[0]) != int or type(data[1]) != int:
        raise TypeError("Expected type tuple[int]")
    # If values less than zero
    if data[0] < 0 or data[1] < 0:
        raise ValueError("Expected positive integers")

class LLStack:

    def __init__(self) -> None:
        """
        Initializes private variables:
        head = None
        size = 0

        Parameters:
        None

        Return:
        None
        
        """
        # Initalize variables
        self.__head:Node|None = None
        self.__size:int = 0
    
    @property
    def size(self) -> int:
        """
        Returns size of LLStack

        Parameters:
        None

        Return:
        self.__size  The total number of nodes in the LLStack
        
        """
        return self.__size
    
    def push(self, data:tuple[int]) -> None:
        """
        Create a node from data and put on the top of the stack

        Parameters:
        data:tuple[int] the data to be added

        Return:
        None
        
        """
        # Check tuple conditions
        tuple_conditions(data)
        # If head is None, set head to the new noee
        if self.__head is None:
            self.__head = Node(data)
        # Else set head to the new node, with it's next value as the current head
        else:
            self.__head = Node(data, self.__head)
        # Increase size by 1
        self.__size += 1

    def pop(self) -> tuple[int]:
        # If head is None, there are no nodes
        if self.__head is None:
            raise IndexError("No nodes found")
        # Store data
        data = self.__head.data
        # Set head to the next value
        self.__head = self.__head.next
        # Decrease size by 1
        self.__size -= 1
        return data

    def __str__(self) -> str:
        # If head is none, there are no nodes
        if self.__head is None:
            return "LLStack is empty"
        # Create a string and store the current node
        res = ""
        curr = self.__head
        # While the next value is not None
        while curr.next is not None:
            # Add the current node data to the beginning of the string formatted below
            res = f" -> ({curr.data[0]},{curr.data[1]})" + res
            curr = curr.next
        # Return the string with the last value at the beginning (with no -> at the beginning)
        return f"({curr.data[0]},{curr.data[1]})" + res