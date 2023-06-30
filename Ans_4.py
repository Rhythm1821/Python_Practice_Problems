# 4. Implement a function to count the occurrence of each element in a list.

from collections import Counter

def occurence_of_each_element(lst):
    return Counter(lst)

lst = [12,12,65,54,54,34,235,54]

func = occurence_of_each_element(lst)

print(func)