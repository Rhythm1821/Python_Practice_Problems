# 31. Write a program to find the sum of all even numbers in a list.

def sum_of_even_num(lst:list):
    total = 0
    total = sum([num if num%2==0 else 0 for num in lst])
    return total

func = sum_of_even_num([1,2,3,4,7,8])
print(func)