def min_num (lst:list) -> int | float:
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    min_num = lst[0]

    for i in lst:
        if i < min_num:
            min_num = i
    return min_num

def max_num (lst:list) -> int | float:
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    max_num = lst[0]

    for i in lst:
        if i > max_num:
            max_num = i
    return max_num

def is_palindrome(str:str) -> bool:
    for i in range(len(str)):
        if str[i] != str[len(str)-i-1]:
            print(str[i] + str[len(str)-i-1])
            return False
        print(str[i] + str[len(str)-i-1])
    return True

def is_palindrome_short(str:str) -> bool:
    return str == str[::-1]

def num_occurences(lst:list, num:int) -> int:
    return lst.count(num)
