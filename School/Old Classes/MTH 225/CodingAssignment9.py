from typing import List

# Create a truth list starting with the bool B
def truth_list(B:bool) -> List[bool]:
    # Create a list with the first element being B
    true_list = [B]
    for n in range(0, 20):
        # Over 20 iterations if the current element is true
        if true_list[n]:
            # Add another element equal to True
            true_list.append(True)
    # Return the list
    return true_list

"""
This function causes an error when run with B = False. This is because it doesn't add any elements. true_list[0] = False,
and we don't do anything when it's False. No new elements added means we get an index error. This is similar to proof by
induction because with proof by induction if the base case is False, when we go to prove by induction it will not work.
Using proof by induction allows us to take a statement that we aren't sure if it's True or False, and we can see that
when that original statement is False, proof by induction will fail.
"""