from typing import List, Any

# Attempt to split vertices into two different groups such that edges only connect between the two groups and not within
# Return true if success and false if fail
def is_bipartite(input_dict:dict, lst1:List[Any] = None, lst2:List[Any] = None) -> bool:
    # Create new lists if no list sent
    if lst1 is None:
        lst1 = []
    if lst2 is None:
        lst2 = []
    # Start looping through the dictionaru
    for key in input_dict:
        # If the key is already in the list
        if key in lst1:
            # Make sure all of the values associated are also included
            all_clear = True
            for value in input_dict[key]:
                if value not in lst2:
                    all_clear = False
            # Then skip to the next loop
            if all_clear:
                continue
        # If the key is already in the list
        if key in lst2:
            # Make sure all of the values associated are also included
            all_clear = True
            for value in input_dict[key]:
                if value not in lst1:
                    all_clear = False
            # Then skip to the next loop
            if all_clear:
                continue
        # All Fit into both lists unless
        allFitList1 = True
        allFitList2 = True
        # They are in the other list
        for value in input_dict[key]:
            if value in lst1:
                allFitList2 = False
            elif value in lst2:
                allFitList1 = False
        # If they don't fit in either list return false
        if not (allFitList1 or allFitList2):
            return False
        # If the values fit into the first list only
        if allFitList1 and not allFitList2:
            # And the key isn't in that list
            if key not in lst1:
                # Add the vertices and keep going
                return is_bipartite(input_dict, list(set(lst1 + input_dict[key])), list(set(lst2 + [key])))
        # If the values fit into the second list only
        if allFitList2 and not allFitList1:
            # And the key isn't in that list
            if key not in lst2:
                # Add the vertices and keep going
                return is_bipartite(input_dict, list(set(lst1 + [key])), list(set(lst2 + input_dict[key])))
        else:
            # Or try both options if they are both feasible
            return is_bipartite(input_dict, list(set(lst1 + input_dict[key])), list(set(lst2 + [key]))) or is_bipartite(input_dict, list(set(lst1 + [key])), list(set(lst2 + input_dict[key])))
    # If you complete the loop then return true
    return True

#Test cases begin here

#is_bipartite({0:[2,3], 1:[3,4], 2:[0], 3:[0,1], 4:[1]}) should return True
print(is_bipartite({0:[2,3], 1:[3,4], 2:[0], 3:[0,1], 4:[1]}))

#is_bipartite({0: [3, 4, 5], 1: [], 2: [4], 3: [0], 4: [0, 2, 5], 5: [0, 4]}) should return False
print(is_bipartite({0: [3, 4, 5], 1: [], 2: [4], 3: [0], 4: [0, 2, 5], 5: [0, 4]}))

#is_bipartite({0: [3, 5], 1: [4], 2: [3, 5], 3: [0, 2], 4: [1], 5: [0, 2]}) should return True
print(is_bipartite({0: [3, 5], 1: [4], 2: [3, 5], 3: [0, 2], 4: [1], 5: [0, 2]}))

#is_bipartite({0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4], 3: [0, 1, 2, 4], 4: [0, 1, 2, 3]}) should return False
print(is_bipartite({0: [1, 2, 3, 4], 1: [0, 2, 3, 4], 2: [0, 1, 3, 4], 3: [0, 1, 2, 4], 4: [0, 1, 2, 3]}))

#is_bipartite({"A": ["X", "Y", "Z"], "B": ["X", "Y", "Z"], "C": ["X", "Y", "Z"], "X": ["A", "B", "C"], "Y": ["A", "B", "C"], "Z": ["A", "B", "C"]}) should return True
print(is_bipartite({"A": ["X", "Y", "Z"], "B": ["X", "Y", "Z"], "C": ["X", "Y", "Z"], "X": ["A", "B", "C"], "Y": ["A", "B", "C"], "Z": ["A", "B", "C"]}))

#is_bipartite({1: [2, 11], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8, 10], 10: [9, 11], 11: [10, 1]}) should return False
print(is_bipartite({1: [2, 11], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8, 10], 10: [9, 11], 11: [10, 1]}))

#is_bipartite({1: [2, 10], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8, 10], 10: [9, 1]}) should return True
print(is_bipartite({1: [2, 10], 2: [1, 3], 3: [2, 4], 4: [3, 5], 5: [4, 6], 6: [5, 7], 7: [6, 8], 8: [7, 9], 9: [8, 10], 10: [9, 1]}))

#is_bipartite({1: [2], 2:[1], 3:[4,5], 4:[3,5], 5:[3,4]}) should return False
print(is_bipartite({1: [2], 2:[1], 3:[4,5], 4:[3,5], 5:[3,4]}))

#is_bipartite({1: [2], 2: [1], 3: [4], 4: [3], 5: [6], 6: [5], 7: [8], 8: [7], 9: [10], 10: [9], 11: [12], 12: [11], 13: [14], 14: [13]}) should return True
print(is_bipartite({1: [2], 2: [1], 3: [4], 4: [3], 5: [6], 6: [5], 7: [8], 8: [7], 9: [10], 10: [9], 11: [12], 12: [11], 13: [14], 14: [13]}))

#is_bipartite({0: [1, 2, 3, 4, 5], 1: [0], 2: [0], 3: [0], 4: [0,5], 5: [0,4]}) should return False
print(is_bipartite({0: [1, 2, 3, 4, 5], 1: [0], 2: [0], 3: [0], 4: [0,5], 5: [0,4]}))