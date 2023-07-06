# 43. Write a program to find the number of occurrences of a given element in a list.

from collections import Counter 

def no_of_occurences(element,lst:list):
    occurences = Counter(lst)
    return occurences[element]
    

func = no_of_occurences(2,[1,2,3,4,2,4,54,43,2])
print(func)