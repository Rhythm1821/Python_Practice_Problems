# 5. Write a Python program to find the second largest number in a list.

def second_larget_number(lst):
    if len(lst) < 2:
        return None
    
    s = set(lst)
    sorted(s)
    l = list(s)
    return l[-2]



lst = [1,2,33,4]
func = second_larget_number(lst)

print(func)