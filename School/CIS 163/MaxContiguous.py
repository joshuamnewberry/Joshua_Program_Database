def max_contiguous(lst:list) -> int|float:
    # Raise type error if not list
    if not isinstance(lst, list):
        raise TypeError
    
    # Return zero if length is zero
    if len(lst) == 0:
        return 0
    
    # Set original values
    currsum = lst[0]
    maxsum = lst[0]

    for i in range(1,len(lst)):
        # Add the next value
        currsum += lst[i]
        # If the current sum is less than the current value
        if lst[i] > currsum:
            # Set the current sum to the current value
            currsum= lst[i]
        # If the current sum is greater than the max
        if currsum > maxsum:
            # Set the max sum to the current sum
            maxsum = currsum
    
    # Return total max contiguous
    return maxsum