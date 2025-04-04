from typing import List

def merge_sort(lst:List[int|float]) -> List[int|float]:
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge_sort_helper(left, right)
    
def merge_sort_helper(lst1:List[int|float], lst2:List[int|float], new_list = None) -> List[int|float]:
    if new_list is None:
        new_list = []
    if len(lst1) == 0:
        return new_list + lst2
    if len(lst2) == 0:
        return new_list + lst1
    if lst1[0] < lst2[0]:
        new_list.append(lst1[0])
        return merge_sort_helper(lst1[1:], lst2, new_list)
    new_list.append(lst2[0])
    return merge_sort_helper(lst1, lst2[1:], new_list)

lst = [85, 24, 63, 45, 17, 31, 96, 50]
print(f"Input data: {lst}")
print(f"Sorted data: {merge_sort(lst)}")