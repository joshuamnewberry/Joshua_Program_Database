from typing import List

def Havel_Hakimi_Helper(input_list:List[int]) -> bool:
    # If first number is negative return false
    if input_list[len(input_list)-1] < 0:
        return False
    # If the first number is bigger than the length of the list - 1 return false
    if input_list[0] > len(input_list)-1:
        return False
    # If the first number is 0
    if input_list[0] == 0:
        return True
    # Loop over 1 - n values in the list where n is the first element of the list
    for i in range(1, input_list[0]+1):
        # Subtract 1
        input_list[i] -= 1
    # Sort reversed and cut off the first element of the list
    input_list = input_list[1:]
    input_list.sort(reverse=True)
    # Send the list back through the method
    return Havel_Hakimi_Helper(input_list)

# Check initial conditions, then send the input to the real function
def Havel_Hakimi(input_list:List[int]) -> bool:
    # Check even degree sum
    if sum(input_list) % 2 == 1:
        return False
    # Check for negative degrees
    for element in input_list:
        if type(element) != int:
            return False
        if element < 0:
            return False
    # Send input to the recursive function
    return Havel_Hakimi_Helper(input_list)

#Test cases begin here

#Havel_Hakimi([2,2])) should return False
print(Havel_Hakimi([2,2]), "| False")

#Havel_Hakimi([1,1,1,1])) should return True
print(Havel_Hakimi([1,1,1,1]), "| True")

#Havel_Hakimi([1,1,1,1,1,1,1,1,1]) should return False
print(Havel_Hakimi([1,1,1,1,1,1,1,1,1]), "| False")

#Havel_Hakimi([6,5,4,3,3,2,1]) should return True
print(Havel_Hakimi([6,5,4,3,3,2,1]), "| True")

#Havel_Hakimi([0,0,0,0,0,0]) should return True
print(Havel_Hakimi([0,0,0,0,0,0]), "| True")

#Havel_Hakimi([6,5,4,3,2,2]) should return False
print(Havel_Hakimi([6,5,4,3,2,2]), "| False")

#Havel_Hakimi([8,7,6,5,4,4,2,1,1]) should return False
print(Havel_Hakimi([8,7,6,5,4,4,2,1,1]), "| False")

#Havel_Hakimi([5,5,5,5,4,3]) should return False
print(Havel_Hakimi([5,5,5,5,4,3]), "| False")

#Havel_Hakimi([5,5,5,5,4,3]) should return True
print(Havel_Hakimi([5,5,5,5,4,4]), "| True")

#Havel_Hakimi([3,3,3,3,3,3,3,3,3,3]) should return True
print(Havel_Hakimi([3,3,3,3,3,3,3,3,3,3]), "| True")