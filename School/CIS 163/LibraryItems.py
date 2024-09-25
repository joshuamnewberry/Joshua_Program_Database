from abc import ABC, abstractmethod

class LibraryItem(ABC):
    
    def __init__(self, item_name:str, borrower_name:str=None) -> None:
        if type(item_name) != str or (type(borrower_name) != str and borrower_name != None):
            raise TypeError
        self.__item_name = item_name
        self.__borrower_name = borrower_name
    
    @property
    def item_name(self) -> str:
        return self.__item_name
    
    @property
    def borrower_name(self) -> str:
        return self.__borrower_name
    @borrower_name.setter
    def borrower_name(self, borrower_name:str|None) -> None:
        if type(borrower_name) != str and borrower_name != None:
            raise TypeError
        self.__borrower_name = borrower_name
    
    @abstractmethod
    def lend_item(self, borrower_name:str) -> None:
        pass

    @abstractmethod
    def return_item(self, return_type_method:str) -> None:
        pass

class Book(LibraryItem):
    
    def __init__(self, item_name:str) -> None:
        super().__init__(item_name)
    
    def __str__(self) -> str:
        if self.borrower_name == None:
            return f"This book {self.item_name} is available"
        return f"This book {self.item_name} is borrowed by {self.borrower_name}"
    
    def lend_item(self, borrower_name:str) -> None:
        self.borrower_name = borrower_name
    
    def return_item(self, return_type_method:str) -> None:
        if return_type_method != "in-person" and return_type_method != "drop":
            raise ValueError
        self.borrower_name = None

class Laptop(LibraryItem):

    def __init__(self, item_name:str, brand_name:str) -> None:
        if type(brand_name) != str:
            raise TypeError
        self.__brand_name = brand_name
        super().__init__(item_name)
    
    def __str__(self) -> str:
        if self.borrower_name == None:
            return f"This {self.__brand_name} Laptop {self.item_name} is available"
        return f"This {self.__brand_name} Laptop {self.item_name} is borrowed by {self.borrower_name}"
    
    @property
    def brand_name(self) -> str:
        return self.__brand_name
    @brand_name.setter
    def brand_name(self, brand_name:str|None) -> None:
        if type(brand_name) != str and brand_name != None:
            raise TypeError
        self.__brand_name = brand_name
    
    def lend_item(self, borrower_name:str) -> None:
        self.borrower_name = borrower_name
    
    def return_item(self, return_type_method:str) -> None:
        if return_type_method != "in-person" and return_type_method != "drop":
            raise ValueError
        self.borrower_name = None