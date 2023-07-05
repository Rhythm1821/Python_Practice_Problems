# 36. Implement a function to calculate the product of all elements in a list.

import math

def prod_of_list(lst:list):
    lst = [num if isinstance(num,(int,float)) else ValueError for num in lst]
    return math.prod(lst)

func = prod_of_list([1,2,3,4])

print(func)