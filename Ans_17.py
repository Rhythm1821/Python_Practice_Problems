# 17. Write a Python program to find the intersection of two lists.

# 17. Write a Python program to find the intersection of two lists.

def find_itersection(lst1,lst2):
    common_elements = []

    for i in set(lst1):
        if i in set(lst2):
            common_elements.append(i)
    return common_elements

lst1 = [1, 2, 3, 4, 5]
lst2 = [4, 5, 6, 7, 8]

func = find_itersection(lst1=lst1,
                        lst2=lst2)

print(func)