# 9. Write a Python program to sort a list of integers in ascending order.

def sort(lst:list):
    lst = [i for i in lst if isinstance(i,int)]
    return sorted(lst)

func = sort([1,22,4,3])

print(func)