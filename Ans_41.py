# 41. Write a Python program to find the smallest missing positive integer in a list.

def smallest_positive_int(lst:list):
    pos_num_set = set()
    for i in lst:
        if i>0:
            pos_num_set.add(i)

    if not pos_num_set:
        return 1
    
    start = min(pos_num_set)
    end = max(pos_num_set)+1
    
    for i in range(start,end):
        if i not in pos_num_set:
            return i
    return end

l1 = [0, -10, 1, 2, 3, 4, 5]


func = smallest_positive_int(l1)
print(func)