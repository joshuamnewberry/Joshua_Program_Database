from abc import ABC, abstractmethod

class Account(ABC):

    def __init__ (self, balance:int|float) -> None:
        if type(balance) != float and type(balance) != int:
            raise TypeError
        self.__balance = balance
    
    @property
    def balance(self) -> int|float:
        return self.__balance
    @balance.setter
    def balance(self, balance:int|float) -> None:
        if type(balance) != float and type(balance) != int:
            raise TypeError
        self.__balance = balance
    
    @abstractmethod
    def deposit(self, deposit:int|float) -> None:
        pass

    @abstractmethod
    def withdraw(self, deposit:int|float) -> None:
        pass

class CheckingAccount(Account):

    def __init__(self, starting_balance:int|float) -> None:
        self.__min_balance = 30
        super().__init__(starting_balance)
    
    def __str__(self) -> str:
        if type(self.balance) == int:
            return f"Checking Account balance is ${self.balance}.00."
        return f"Checking Account balance is ${self.balance}."
    
    @property
    def min_balance(self) -> int:
        return self.__min_balance

    def deposit(self, deposit:int|float) -> None:
        if type(deposit) != float and type(deposit) != int:
            raise TypeError
        if deposit < 0:
            raise ValueError
        self.balance = self.balance + deposit
    
    def withdraw(self, withdraw:int|float) -> None:
        if type(withdraw) != float and type(withdraw) != int:
            raise TypeError
        if withdraw < 0 or (self.balance - withdraw) < self.__min_balance:
            raise ValueError
        self.balance = self.balance - withdraw

class SavingsAccount(Account):

    def __init__(self, starting_balance:int|float) -> None:
        super().__init__(starting_balance)
    
    def __str__(self) -> str:
        if type(self.balance) == int:
            return f"Savings Account balance is ${self.balance}.00."
        return f"Savings Account balance is ${self.balance}."

    def deposit(self, deposit:int|float) -> None:
        if type(deposit) != float and type(deposit) != int:
            raise TypeError
        if deposit < 0:
            raise ValueError
        self.balance = self.balance + deposit
    
    def withdraw(self, withdraw:int|float) -> None:
        raise ValueError