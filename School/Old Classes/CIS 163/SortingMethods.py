from typing import List
from random import randint

def bubble_sort(lst:List[int|float]) -> List[int|float]:
    sorted = False
    for i in range(0, len(lst)):
        sorted = True
        for i in range(1, len(lst)-i):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                sorted = False
        if sorted:
            return i

def reversing_bubble_sort(lst:List[int|float]) -> List[int|float]:
    sorted = False
    for i in range(0, len(lst)):
        sorted = True
        for j in range(1+i, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                sorted = False
        if sorted:
            return i*2 - 1
        sorted = True
        for j in range(len(lst)-2-i, 0+i, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                sorted = False
        if sorted:
            return i*2

def selection_sort(lst:List[int|float]) -> List[int|float]:
    for i in range(0, len(lst)):
        mindex = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[mindex]:
                mindex = j
        if i != mindex:
            lst[i], lst[mindex] = lst[mindex], lst[i]

def insertion_sort(lst:List[int|float]) -> List[int|float]:
    for i in range(0, len(lst)-1):
        j = i+1
        while j >= 1 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1

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

def quick_sort_helper(lst:List[int|float], pivot:int, left:int, right:int) -> List[int|float]:
    end = right
    if right - pivot == 1:
        if lst[right] < lst[pivot]:
            lst[right], lst[pivot] = lst[pivot], lst[right]
        return
    if right - pivot < 1:
        return
    while left <= right:
        while lst[left] <= lst[pivot] and left <= right:
            left += 1
        while lst[right] >= lst[pivot] and left <= right:
            right -= 1
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
    lst[left-1], lst[pivot] = lst[pivot], lst[left-1]
    quick_sort_helper(lst, pivot, pivot+1, left-2)
    quick_sort_helper(lst, left, left+1, end)
    
def quick_sort(lst:List[int|float]) -> List[int|float]:
    quick_sort_helper(lst, 0, 1, len(lst)-1)