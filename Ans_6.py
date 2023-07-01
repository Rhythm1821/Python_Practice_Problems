# 6. Implement a function to remove duplicate elements from a list.

def remove_duplicate(lst):
    lst = list(set(lst))
    return lst

func = remove_duplicate([1,1,4,9,8,9,9,9])

print(func)