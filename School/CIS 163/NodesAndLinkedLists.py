from typing import Any

class Node:
    def __init__(self, ele, next = None) -> None:
        self.value = ele
        self.next = next

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = head

    def add_node(self, new_node:Node|Any, index:int = -1) -> None:
        if type(new_node) != Node:
            new_node = Node(new_node)
        if type(index) != int:
            raise TypeError("Index must be an integer")
        if self.head is None:
            if index > 0:
                raise ValueError(f"No nodes found: Cannot add at index {index}")
            self.head = new_node
        elif index == -1:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
        else:
            curr = self.head
            while index != 1:
                curr = curr.next
                index -= 1
            next = curr.next
            curr.next = new_node
            new_node.next = next
    
    def remove_node_index(self, index:int = -1) -> None:
        if type(index) != int:
            raise TypeError("Index must be an integer")
        if self.head is None:
            if index > 0:
                raise ValueError(f"No nodes found: Cannot add at index {index}")
        elif index == -1:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.prev.next = None
        else:
            curr = self.head
            while index != 1:
                curr = curr.next
                index -= 1
            curr.next = curr.next.next
            if curr.next is not None:
                curr.next.prev = curr
    
    def remove_node_val(self, del_val:Any) -> None:
        if self.head is None:
            raise ValueError("No nodes found")
        if self.head.value == del_val:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next.value != del_val:
            curr = curr.next
        curr.next = curr.next.next
    
    def reverse_list(self):
        prev = self.head
        curr = self.head.next
        while curr.next != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr =  next
        self.head.next = None
        curr.next = prev
        self.head = curr
        return self.head
    
    def find_middle(self):
        index = 0
        if self.head is None:
            return None
        curr = self.head
        while curr != None:
            index += 1
            curr = curr.next
        index = int(index/2)
        curr = self.head
        while index > 0:
            index -= 1
            curr = curr.next
        return curr.value

    def has_cycle(self):
        if self.head is None:
            return False
        curr = self.head
        lst = []
        while curr != None:
            if curr in lst:
                return True
            lst.append(curr)
            curr = curr.next
        return False
    
    def __str__(self) -> str:
        res = ""
        if self.head is None:
            return res
        else:
            curr = self.head
            while curr != None:
                res += str(curr.value) + " "
                curr = curr.next
            return res

class DoubleNode:
    def __init__(self, ele, prev = None, next = None) -> None:
        self.value = ele
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self, head = None) -> None:
        self.head = head

    def add_node(self, new_node:DoubleNode|Any, index:int = -1) -> None:
        if type(new_node) != DoubleNode:
            new_node = DoubleNode(new_node)
        if type(index) != int:
            raise TypeError("Index must be an integer")
        if self.head is None:
            if index > 0:
                raise ValueError(f"No nodes found: Cannot add at index {index}")
            self.head = new_node
        elif index == -1:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        else:
            curr = self.head
            while index != 1:
                curr = curr.next
                index -= 1
            new_node.next = curr.next
            curr.next = new_node
            new_node.prev = curr
            if new_node.next is not None:
                new_node.next.prev = new_node 

    def remove_node_index(self, index:int = -1) -> None:
        if type(index) != int:
            raise TypeError("Index must be an integer")
        if index < -1:
            raise ValueError("Index must be greater or equal to -1")
        if self.head is None:
            if index > 0:
                raise ValueError(f"No nodes found: Cannot remove at index {index}")
        elif index == -1:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.prev.next = None
        else:
            curr = self.head
            while index != 1:
                curr = curr.next
                index -= 1
            curr.next = curr.next.next
            if curr.next is not None:
                curr.next.prev = curr
    
    def remove_node_val(self, del_val:Any) -> None:
        if self.head is None:
            raise ValueError("No nodes found")
        if self.head.value == del_val:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next.value != del_val:
            curr = curr.next
        curr.next = curr.next.next
    
    def __str__(self) -> str:
        res = ""
        if self.head is None:
            return res
        else:
            curr = self.head
            while curr != None:
                res += str(curr.value) + " "
                curr = curr.next
            return res