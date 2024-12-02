from typing import Any

class Node:
    def __init__(self, ele, next = None) -> None:
        self.value = ele
        self.next = next

class LinkedList:
    def __init__(self, head = None, length = 0) -> None:
        self.head = head
        self.length = length

    def add_node(self, new_node:Node|Any, index:int = -1) -> None:
        if type(new_node) != Node:
            new_node = Node(new_node)
        if type(index) != int:
            raise TypeError("Index must be an integer")
        if self.head is None:
            if index > 0:
                raise ValueError(f"No nodes found: Cannot add node at index {index}")
            self.head = new_node
        elif index == -1:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            self.length += 1
        else:
            if index >= self.length:
                raise IndexError(f"List length of {self.length}, index {index} out of bounds")
            curr = self.head
            while index != 1:
                curr = curr.next
                index -= 1
            next = curr.next
            curr.next = new_node
            new_node.next = next
            self.length += 1
    
    def remove_node(self, del_val:Node|Any) -> None:
        if self.head is None:
            raise ValueError("No nodes found")
        if type(del_val) == Node:
            if self.head == del_val:
                self.head = self.head.next
                self.length -= 1
            else:
                curr = self.head
                if curr.next is None:
                    raise ValueError("Node not found")
                while curr.next != del_val:
                    curr = curr.next
                    if curr.next is None:
                        raise ValueError("Node not found")
                curr.next = curr.next.next
                self.length -= 1
        else:
            if self.head.value == del_val:
                self.head = self.head.next
                self.length -= 1
            else:
                curr = self.head
                if curr.next is None:
                    raise ValueError("Node not found")
                while curr.next.value != del_val:
                    curr = curr.next
                    if curr.next is None:
                        raise ValueError("Node not found")
                curr.next = curr.next.next
                self.length -= 1
    
    def remove_node_index(self, index:int = -1) -> None:
        if type(index) != int:
            raise TypeError("Index must be an integer")
        if index >= self.length:
            raise IndexError(f"List length of {self.length}, index {index} out of bounds")
        if self.head is None:
            raise ValueError(f"No nodes found: Cannot add at index {index}")
        elif index == -1 or index == self.length-1:
            if self.length == 1:
                self.head = None
            elif self.length == 2:
                self.head.next = None
            else:
                curr = self.head
                while curr.next.next is not None:
                    curr = curr.next
                curr.next = curr.next.next
            self.length -= 1
        else:
            curr = self.head
            while index != 1:
                curr = curr.next
                index -= 1
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
    
    def merge_in(self, other):
        curr1 = self.head
        curr2 = other.head
        if curr2 is None:
            return
        if curr1 is None:
            self.head = other.head
            self.tail = other.tail
            self.size = other.size
            self.size += other.size
            other.head = None
            other.tail = None
            other.size = 0
            return
        while curr1.next is not None and curr2.next is not None:
            next1 = curr1.next
            next2 = curr2.next
            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2
        if curr1.next is None:
            curr1.next = curr2
            self.tail = other.tail
        if curr2.next is None:
            next1 = curr1.next
            curr1.next = curr2
            curr2.next = next1
        self.size += other.size
        other.head = None
        other.tail = None
        other.size = 0
    
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
    def __init__(self, ele, next = None, prev = None) -> None:
        self.value = ele
        self.next = next
        self.prev = prev

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
                if curr is None:
                    raise IndexError(f"List length less than {index}")
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
            if curr is None:
                raise ValueError("Node not found")
        curr.next = curr.next.next
    
    def remove_node_obj(self, del_node:DoubleNode) -> None:
        if self.head is None:
            raise ValueError("No nodes found")
        if self.head.value == del_node:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next != del_node:
            curr = curr.next
            if curr is None:
                raise ValueError("Node not found")
        if curr.next != None:
            curr.next = curr.next.next
            return
        curr.next = None
    
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