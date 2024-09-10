def even(n) -> list:
    a = []
    #Loop over half of integers from 0 to (inclusive) and multiply all values by two
    #to return all even integers from 0 to n (inclusive)
    for i in range(0, int(n/2) + 1):
        a.append(i*2)
    return a

def firstLastEqual(A:list, B:list) -> bool:
    #If the first value of each list are equal return true
    if A[0] == B[0]:
        return True
    #If the last value of each list are equal return true
    if A[len(A)-1] == B[len(B)-1]:
        return True
    #If you arrive to this line return false
    return False

def findPudding(D:dict) -> list | bool:
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
