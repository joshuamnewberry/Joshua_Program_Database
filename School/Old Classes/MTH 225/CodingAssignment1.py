from typing import List, Any

# Returns a list of all even integers from 0 to n inclusive
def even(n) -> list:
    # Create  new list
    a = []
    #Loop over half of integers from 0 to n inclusive
    for i in range(0, int(n/2) + 1):
        # Multiply i by 2 and add to the list
        a.append(i*2)
    # Return the list
    return a

# Return true if the first or last elements of each list are equal
def firstLastEqual(A:list, B:list) -> bool:
    #If the first value of each list are equal return true
    if A[0] == B[0]:
        return True
    #If the last value of each list are equal return true
    if A[len(A)-1] == B[len(B)-1]:
        return True
    #If you arrive to this line return false
    return False

# Return a list beggining with True, and including all keys of the value pudding in the dictionary D
# If there are no instances of pudding then return False
def findPudding(D:dict) -> bool|List[bool|Any]:
    #Initialize list to be returned if we find the value "pudding"
    a = [True]
    for i in D:
        #If the value at the key i equals pudding at the key to the list
        if D[i] == "pudding":
            a.append(i)
    #If we didn't find pudding the list will have a length of one so return False
    if len(a) == 1:
        return False
    #If we found pudding then return the list with all key values giving pudding
    return a