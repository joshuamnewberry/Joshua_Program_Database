def sumOfNum(n:int) -> int:
    total = n
    for i in range(1, n):
        total += i
    return total

def recursiveSum(n:int) -> int:
    if n == 1:
        return 1
    return n + recursiveSum(n-1)

def factorial(n:int) -> int:
    total = n
    for i in range(2, n):
        total *= i
    return total

def recursiveFactorial(n:int) -> int:
    if n == 2:
        return 2
    return n * recursiveFactorial(n-1)

def fibonacci(n:int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    prev = 1
    total = 1
    for _ in range(1, n-2):
        temp = total
        total += prev
        prev = temp
    return total

def recursiveFibonacci(n:int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 1
    return recursiveFibonacci(n-1) + recursiveFibonacci(n-2)

# This one comepletely mutilates the list
def recursiveListSum(lst:list) -> float:
    if len(lst) == 1:
        return lst[0]
    sum = lst[0] + lst[1]
    lst.remove(lst[1])
    lst[0] = sum
    return recursiveListSum(lst)

# Correct version
def recursiveListSum(lst:list) -> float:
    if len(lst) == 1:
        return lst[0]
    return lst[0] + recursiveListSum(lst[1:])

def recursiveCombineLists(lst:list) -> list:
    if len(lst) == 0:
        return []
    if type(lst[0]) == list:
        return recursiveCombineLists(lst[0]) + recursiveCombineLists(lst[1:])
    return [list[0]] + recursiveCombineLists(lst[1:])

def recursivePowerFunct(m:int, n:int) -> int:
    if n == 1:
        return m
    return m * recursivePowerFunct(m, n-1)