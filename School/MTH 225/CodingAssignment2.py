# Return a list of values that are included in both lists
def intersect(list1:list, list2:list) -> list:
    # Create an empty list
    intersectList = []
    # For each element i in list 1, check if it is in list 2, if True add to the intersection list
    for i in list1:
        if i in list2:
            intersectList.append(i)
    # Return the completed list
    return intersectList

# Return a list of values that are in either list with no duplicates
def union(list1:list, list2:list) -> list:
    # Create a new list with all values from list1
    unionList = list1
    # For each element i in list 2, check if it is not in list 2, if True add to the union list
    for i in list2:
        if i not in unionList:
            unionList.append(i)
    return unionList

# Return a True if both lists contain exactly the same elements, otherwise return False
def equal(list1:list, list2:list) -> list:
    # If the length of both lists are not the same, they are not equal so return False
    if len(list1) != len(list2):
        return False
    # For each element i in list1, check if it is not in list 2, if True return False as they do not contain equal elements
    for i in list1:
        if i not in list2:
            return False
    # If you get to the end of the for loop, then the lists are the same so return True
    return True