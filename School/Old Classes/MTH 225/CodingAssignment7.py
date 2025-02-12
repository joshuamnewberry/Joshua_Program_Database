from typing import List

# Generate an arithmetic sequence starting at initial that changes at a rate of difference and goes till the last_index returned as a list
def generate_arithmmetic_seq(initial:int|float, difference:int|float, last_index:int) -> List[int|float]:
    # If last index is negative raise value error
    if last_index < 0:
        raise ValueError
    # Create a list starting with the inital value
    lst = [initial]
    # Loop last_index number of times
    for _ in range (0, last_index):
        # Append the last number in the list plus the difference
        lst.append(lst[-1] + difference)
    # Return the completed list
    return lst

# Generate a geometric sequence starting at initial that changes at a ratio and goes till the last_index returned as a list
def generate_geometric_seq(initial:int|float, ratio:int|float, last_index:int) -> List[int|float]:
    # If last index is negative raise value error
    if last_index < 0:
        raise ValueError
    # Create a list starting with the inital value
    lst = [initial]
    # Loop last_index number of times
    for _ in range (0, last_index):
        # Append the last number in the list times the ratio
        lst.append(lst[-1] * ratio)
    # Return the completed list
    return lst

# Generate a patial sum sequence of a list S returned as a list
def generate_partialSum_seq(S:List[int|float]) -> List[int|float]:
    # If last index is negative raise value error
    if len(S) <= 1:
        return S
    # Create a list starting with the inital value
    lst = [S[0]]
    # Loop over the number of items in S (except the first one)
    for i in range (1, len(S)):
        # Append the last number in the list plus the next number in S
        lst.append(lst[-1] + S[i])
    # Return the completed list
    return lst