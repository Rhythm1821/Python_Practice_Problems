# 25. Write a Python program to merge two sorted lists into a single sorted list.


def merge_list(lst1,lst2)->list:
    lst1_valid = all(isinstance(i,(int,float)) for i in lst1)
    lst2_valid = all(isinstance(i,(int,float)) for i in lst2)

    if lst1_valid and lst2_valid:
        return sorted(lst1)+sorted(lst2)
    else:
        raise ValueError

func = merge_list([3,2,5,1,4],[7,9,6,10,8])

print(func)