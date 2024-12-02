from typing import List

# Perform n differences to the sequence recursively
def perform_difference(seq:List[int|float], n:int = 1) -> List[int|float]:
    # Base condition: if n equal zero return the sequence
    if n == 0:
        return seq
    diff = []
    # Perform the difference
    for i in range(1, len(seq)):
        diff.append(seq[i]-seq[i-1])
    # Return the method with the new difference sequence and n-1
    return perform_difference(diff, n-1)

# Check that the sequence has a constant difference sequence after n differences
def check_difference(seq:List[int|float], n:int = 2) -> bool:
    # Perform n differences (default of 2)
    diff = perform_difference(seq, 2)
    for i in range(1, len(seq)):
        # If the two numbers are not equal, or are equal to zero return False
        if diff[i] != diff[i-1] or diff[i] == 0:
            return False
    # If all numbers in the difference sequence were constant non zero return True
    return True