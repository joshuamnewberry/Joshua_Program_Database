from typing import List

# Cross multiply two lists and return it as a 2D list
def multiplyList(a:List[int|float], b:List[int|float]) -> List[List[int|float]]:
    lst:List[List[None]] = [[None for i in range(len(a))] for j in range(len(b))]
    for y in range(len(b)):
        for x in range(len(a)):
            lst[y][x] = a[x] * b[y]
    return lst