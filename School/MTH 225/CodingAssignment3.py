# This method returns a list containing f^-1(a)
def inverseImage(f:dict, a) -> list:
    # Create a new list
    lst = []
    # Create variables referencing the keys list and values list
    key_list = list(f.keys())
    value_list = list(f.values())
    # For the values in f, if the value is equal to a and not already in the list, add it
    for i in range(0, len(f)):
        if value_list[i] == a and key_list[i] not in lst:
            lst.append(key_list[i])
    # Return the completed list
    return lst

# This method returns True if the dictionary is injective, and False otherwise
def injective(f:dict) -> bool:
    # Create a new list
    outputs = []
    # For the values in f, if the output is not in the list, add it. If it is, return False
    for i in f:
        if f[i] not in outputs:
            outputs.append(f[i])
        else:
            return False
    # If we exit the loop without returning False, then return True
    return True

# This method returns True if their is an input for all outputs in the codomain, otherwise returns False
def surjective(f:dict, C:list) -> bool:
    # Create a temporary list from the input list
    lst = list(C.copy())
    # For the values in f, if the output is in the list of codomain, remove it from the list
    for i in f:
        # If in the value of f is in lst remove it
        if f[i] in lst:
            lst.remove(f[i])
    # After exiting the loop, if the list is empty return True
    if lst == []:
        return True
    # Otherwise return False
    return False