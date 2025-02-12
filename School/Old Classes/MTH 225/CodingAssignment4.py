# Converts a list of numbers from 1 to n to a bit string where those numbers are the positions of 1's
def setToBit(lst:list, n:int) -> list:
    # Create a new list
    bit = []
    # Loop from 0 to n
    for i in range(0, n):
        # If i-1 is in the list add a 1 to the bit string
        if i+1 in lst:
            bit.append(1)
        # Otherwise add a 0 to the bit string
        else:
            bit.append(0)
    # Return the bit string
    return bit

# Converts a list of 'up' and 'right' to a list of the index + 1 of 'up' values
def latticeToSet(lst:list, n:int) -> list:
    # Create a new list
    set = []
    # Loop from 0 to n
    for i in range(0, n):
        # If the value at i is equal to up add the index + 1 to the set
        if lst[i] == "up":
            set.append(i+1)
    # Return the set
    return set

# Converts a list of 0's and 1's to a list of 'up' and 'right' where 0 = 'right' and 1 = 'up'
def bitToLattice(lst:list) -> list:
    # Create a new list
    lattice = []
    # Loop over the values of lst
    for i in lst:
        # If i equals one add up to the list
        if i == 1:
            lattice.append("up")
        # Otherwise add right to the list
        else:
            lattice.append("right")
    # Return the lattice path
    return lattice