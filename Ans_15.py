# 15. Write a program to find the median of a list of numbers.
import numpy as np

lst = input().split()

try:
    lst = list(map(int,lst))
    median = np.median(lst)

    print(median)
    
except Exception as e:
    raise e
    
