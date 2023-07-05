# 35. Write a program to check if a given number is a perfect square.

import math

def perfect_square_check(num):
    return True if math.sqrt(num)==int(math.sqrt(num)) else False

func = perfect_square_check(36)  

print(func)

