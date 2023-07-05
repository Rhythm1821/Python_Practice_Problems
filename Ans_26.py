# 26. Implement a function to find the mode of a list of numbers.

from statistics import mode

def mode_of_list(lst:list):
    return mode(lst)

func = mode_of_list([1, 2, 3, 3, 4, 4, 4, 5, 5, 6,4,4,5,5,5,55,5,5])    

print(func)