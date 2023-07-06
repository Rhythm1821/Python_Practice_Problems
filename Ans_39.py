# 39. Write a program to find the sum of digits of a given number.

def sum_of_digits(n:int):
    total = 0
    for i in str(n):
        total+=int(i)
    return total

func = sum_of_digits(55)

print(func)