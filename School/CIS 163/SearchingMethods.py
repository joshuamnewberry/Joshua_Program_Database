from typing import List

def binarySearch(lst:List[int|float], val:int|float, index:int = 0) -> int:
    if len(lst) == 0:
        return -1
    mid_index = len(lst) // 2
    if val == lst[mid_index]:
        return index + mid_index
    if val < lst[mid_index]:
        return binarySearch(lst[0:mid_index], val)
    else:
        return binarySearch(lst[mid_index+1:], val, mid_index+1)