from typing import Any

class Node:
    
    def __init__(self, val:Any, next = None) -> None:
        self.val = val
        self.next = next

class Stack:

    def __init__(self) -> None:
        self.__head = None
        self.__length = 0
        
    def push(self, val) -> None:
        if self.__head is None:
            self.__head = Node(val)
            self.__length = 1
        else:
            self.__head = Node(val, self.__head)
            self.__length += 1
    
    def pop(self) -> Any:
        if self.__head is None:
            print("The Stack is now empty! No item is popped!")
            return None
        val = self.__head.val
        self.__head = self.__head.next
        self.__length -= 1
        return val
    
    def top(self) -> Any:
        if self.__head is None:
            return None
        return self.__head.val
    
    def getSize(self) -> int:
        return self.__length
    
    def empty(self) -> bool:
        return self.__length == 0

S = Stack()

for i in range(0, 5):
    S.push(i)
    print(S.top(), end=" ")
print("have been pushed!")
print(f"Current stack size is {S.getSize()}")
for i in range(0, 5):
    print(S.top(), end=" ")
    S.pop()
print("have been popped!")
S.pop(); # an additional pop() to test error handling of pop() function, since the stack is empty
print(f"Current stack size is {S.getSize()}")
if S.empty():
    print("Current stack is empty!")
else:
    print("Current Stack is not empty!")