# Converts a bit string to a list of number of trees in a yard
def bitToTy(lst:list) -> list:
    # Create a new list
    yardList = []
    # Create a counter variable
    currentTrees = 0
    # Loop over the length of the list
    for i in range(0, len(lst)):
        # If the list at i equals 1 (fence) add the current trees to the list and reset the variable
        if lst[i] == 1:
            yardList.append(currentTrees)
            currentTrees = 0
        # Otherwise add 1 to the tree variable
        else:
            currentTrees += 1
    # After exiting add the current trees to the list
    yardList.append(currentTrees)
    # Return the list
    return yardList

# Converts a list of number of trees in a yard to a bit string
def tyToBit(lst:list) -> list:
    # Create a new list
    bitList = []
    # Loop through the list
    for i in lst:
        # Add as many zeros as there are trees
        for _ in range(0, i):
            bitList.append(0)
        # Add a fence
        bitList.append(1)
    # Get rid of the extra fence from the last iteration
    bitList.pop()
    # Return the list
    return bitList