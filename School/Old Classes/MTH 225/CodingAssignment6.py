from typing import List, Any

# Returns a Sequence of terms using a recursive formula where An = C1 * An-1 + C2 * An-2
def recursiveSequence(n:int, a0:int|float, a1:int|float, c1:int|float, c2:int|float) -> list:
    # If n is less than 0 return an empty list
    if n < 0:
        return []
    # Return the first term in the sequence plus the method again where the first term is a1
    # And the second term is calculated by the formula. Input n-1 so that when n < 0 we will quit
    return [a0] + recursiveSequence(n-1, a1, c1 * a1 + c2 * a0, c1, c2)

# Returns a list of all subsets of A with cardinality 2
def listPairs(A:list) -> List[List[Any]]:
    # Create a new list
    lst = []
    # Loop over all indexes in A
    for i in range(0, len(A)):
        # Loop over all indexes from i+1 to the end of A
        for j in range(i+1, len(A)):
            # Add a list of the element at i, the element at j
            lst.append([A[i], A[j]])
    # Return the completed list
    return lst

# Returns a list of all subsets of A with cardinality 3
def listTriples(A:list) -> List[List[Any]]:
    # Create a new list
    lst = []
    # Loop over all indexes in A
    for i in range(0, len(A)):
        # Loop over all indexes from i+1 to the end of A
        for j in range(i+1, len(A)):
            # Loop over all indexes from j+1 to the end of A
            for k in range(j+1, len(A)):
                # Add a list of the element at i, the element at j, the element at k
                lst.append([A[i], A[j], A[k]])
    # Return the completed list
    return lst