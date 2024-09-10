class NonPositiveError(Exception):
    def __init__(self):
        pass
    def __str__(self) -> str:
        return "Input must be a positive number"

class LowBalanceError(Exception):
    def __init__(self):
        pass
    def __str__(self) -> str:
        return "Insufficient Balance to withdraw"

class Bank:

    name_error = "Not a valid name"
    dep_error = "Not a valid deposit"

    def __init__(self, name:str=None, deposit:float=None) -> None:
        try:
            if name == None:
                name = str(input("Enter Name: "))
            self.name = str(name)
        except:
            print(Bank.name_error)
        try:
            if deposit == None:
                deposit = float(input("Enter Deposit amount: "))
            if deposit <= 0:
                raise NonPositiveError
            self.balance = float(deposit)
        except ValueError or TypeError:
            print(Bank.dep_error)
        except NonPositiveError as msg:
            print(msg)
    
    def __str__(self) -> str:
        return f"Name: {self.name}  Balance: {self.balance}"
    
    def deposit(self, deposit:float=None) -> None:
        try:
            if deposit == None:
                deposit = float(input("Enter Deposit amount: "))
            if deposit <= 0:
                raise NonPositiveError
            self.balance += float(deposit)
            print("New balance is:", self.balance)
        except ValueError or TypeError:
            print(Bank.dep_error)
        except NonPositiveError as msg:
            print(msg)

    def withdraw(self, withdraw:float=None) -> None:
        try:
            if withdraw == None:
                withdraw = float(input("Enter Withdraw amount: "))
            if withdraw <= 0:
                raise NonPositiveError
            if withdraw > self.balance:
                raise LowBalanceError
            self.balance -= float(withdraw)
            print("New balance is:", self.balance)
        except ValueError or TypeError:
            print(Bank.dep_error)
        except NonPositiveError as msg:
            print(msg)
        except LowBalanceError as msg:
            print(msg, str(withdraw), "dollars")
    
    def renameCustomer(self, newName:str=None) -> None:
        try:
            if newName == None:
                newName = str(input("Enter new name: "))
            self.name = str(newName)
            print("Customer's new Name is:", self.name)
        except:
            print(Bank.name_error)
    
    def get_name(self) -> str:
        return self.name
    
    def get_balance(self) -> float:
        return self.balance
