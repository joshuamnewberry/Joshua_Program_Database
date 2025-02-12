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