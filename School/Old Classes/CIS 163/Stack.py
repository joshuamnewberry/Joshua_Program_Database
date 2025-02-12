from typing import Any
from Queue import Queue

class Stack:
    def __init__(self, lst:list = None) -> None:
        if lst == None:
            lst = []
        if type(lst) != list:
            return TypeError
        self.__lst = lst
    
    @property
    def stack(self) -> list:
        return self.__lst
    @stack.setter
    def stack(self, lst:list) -> None:
        if type(lst) != list:
            return TypeError
        self.__lst = lst
    
    @property
    def size(self) -> int:
        return len(self.__lst)
    
    @property
    def top(self) -> Any:
        return self.__lst[self.size-1]
    
    def push(self, element:Any) -> None:
        self.__lst.append(element)
    
    def pop(self, num:int = 1) -> Any:
        try:
            if num > self.size:
                raise ValueError
        except ValueError:
            print("Not enough values in the stack")
        lst = []
        for _ in range (0, num):
            lst.append(self.__lst.pop())
        if len(lst) == 1:
            return lst[0]
        return lst