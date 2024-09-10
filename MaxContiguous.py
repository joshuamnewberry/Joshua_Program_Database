def max_contiguous(lst):
    if not isinstance(lst, list):
        raise TypeError
    
    if len(lst) == 0:
        return 0

    curmax = lst[0]
    totalmax = lst[0]

    for i in range(1,len(lst)):
        curmax += lst[i]
        if lst[i] > curmax:
            curmax = lst[i]
        if curmax > totalmax:
            totalmax = curmax

    return totalmax