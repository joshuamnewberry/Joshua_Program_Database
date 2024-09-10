def multiplyList(a:list, b:list) -> list:
    lst = [[0 for i in range(len(a))] for j in range(len(b))]
    for y in range(len(b)):
        for x in range(len(a)):
            lst[y][x] = a[x]*b[y]
    return lst
