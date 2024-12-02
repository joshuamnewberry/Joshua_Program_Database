from __future__ import annotations
from typing import Optional, List
class Node:
    """
    Node in the LLStack.

    Attributes
    ----------
    data : tuple
        Tuple in the form (row,col) representing location in maze.
    next : Node
        Next node in the LLStack.
    """

    def __init__(self, data: tuple[int], next_node: Optional[Node] = None):
        """
        Constructor for Node.

        Parameters
        ----------
        data : tuple
            Tuple in the form (row,col) representing location in maze.
        next_node : Node, optional
            Next node in the LLStack.
        """

        self.data = data
        self.next = next_node

    def __str__(self):
        """
        String representation of Node

        Returns
        ----------
        str
            String representation of location in maze formatted in form "(row,col)".
        """

        return f'({self.data[0]},{self.data[1]})'
