# 11. Write a program to find the common elements between two lists.

def common_elements(lst1:list,lst2:list):
    common_int = []
    # for i in lst1:
    [common_int.append(i) for i in lst1 if i in lst2 and i not in common_int]
    return common_int

func = common_elements([10,2,34,4],[4,3,2,1])

print(func)