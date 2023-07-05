# 33. Write a Python program to remove duplicates from a list while preserving the order.

def remove_duplicate(lst:list):
    lst = [num if isinstance(num,(int,float)) else ValueError for num in lst]
    if ValueError not in lst:
        return list(set(lst))
    else:
        raise ValueError

func = remove_duplicate([1,1,2,3,3])
print(func)
