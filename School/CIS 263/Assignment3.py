from typing import Any

class Queue:
    def __init__(self, lst:list = None) -> None:
        if lst == None:
            lst = []
        if type(lst) != list:
            return TypeError
        self.__lst = lst
    
    @property
    def queue(self) -> list:
        return self.__lst
    @queue.setter
    def queue(self, lst:list) -> None:
        if type(lst) != list:
            return TypeError
        self.__lst = lst
    
    @property
    def size(self) -> int:
        return len(self.__lst)
    
    @property
    def front(self) -> Any:
        if self.size == 0:
            raise IndexError
        return self.__lst[0]
    
    @property
    def rear(self) -> Any:
        if self.size == 0:
            raise IndexError
        return self.__lst[self.size-1]
    
    def add(self, element:Any) -> None:
        self.__lst.append(element)
    
    def remove(self, num:int = 1) -> Any|list:
        try:
            if num > self.size:
                raise ValueError
        except ValueError:
            print("Not enough values in the queue")
        lst = []
        for _ in range (0, num):
            lst.append(self.__lst.pop(0))
        if len(lst) == 1:
            return lst[0]
        return lst

class treeNode:
    def __init__(self, ele, left = None, right = None) -> None:
        self.value = ele
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, head = None, length = 0) -> None:
        self.head = head
        self.length = length
    
    def __str__(self) -> str:
        return self.level_order()

    def add_node(self, new_node:treeNode|int|float) -> None:
        if type(new_node) != treeNode:
            if type(new_node) != int and type(new_node) != float:
                raise TypeError("Must be type treeNode, int, or float")
            new_node = treeNode(new_node)
        if self.head is None:
            self.head = new_node
            self.length = 1
        else:
            curr = self.head
            while True:
                if curr.value == new_node.value:
                    raise ValueError("Must be a unique number")
                if curr.value > new_node.value:
                    if curr.left is not None:
                        curr = curr.left
                    else:
                        curr.left = new_node
                        self.length += 1
                        return
                else:
                    if curr.right is not None:
                        curr = curr.right
                    else:
                        curr.right = new_node
                        self.length += 1
                        return
    
    def level_order(self) -> str:
        if self.head is None:
            return ""
        curr = self.head
        queue = Queue()
        res = str(self.head.value)
        queue.add(curr.left)
        queue.add(curr.right)
        while queue.size > 0:
            curr = queue.remove()
            if curr is not None:
                res += " " + str(curr.value)
                queue.add(curr.left)
                queue.add(curr.right)
        return res
    
    def post_order(self) -> str:
        return self.post_order_helper(self.head)
    
    def post_order_helper(self, curr:treeNode) -> str:
        if curr is None:
            return ""
        return self.post_order_helper(curr.left) + self.post_order_helper(curr.right) + f" {curr.value}"
    
    def num_nodes(self) -> int:
        return self.num_nodes_helper(self.head)
    
    def num_nodes_helper(self, curr:treeNode) -> int:
        if curr is None:
            return 0
        return 1 + self.num_nodes_helper(curr.left) + self.num_nodes_helper(curr.right)
    
    def num_leaves(self) -> int:
        return self.num_leaves_helper(self.head)
    
    def num_leaves_helper(self, curr:treeNode) -> int:
        if curr is None:
            return 0
        if curr.left is None and curr.right is None:
            return 1
        return self.num_leaves_helper(curr.left) + self.num_leaves_helper(curr.right)

bt = BinarySearchTree()
lst = [20,10,3,35,2,62,39,21,1,78,16,11,50,76,28]
for i in lst:
    bt.add_node(i)
print("bt = 20 10 3 35 2 62 39 21 1 78 16 11 50 76 28")
print(f"\nlevel order: {bt}")
print (f"\npost_order: {bt.post_order()}")
print(f"\nnum nodes: {bt.num_nodes()}")
print(f"\nnum leaves: {bt.num_leaves()}")