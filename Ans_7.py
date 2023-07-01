# 7. Write a program to calculate the factorial of a given number.

def factorial(n:int):
    n*=factorial(n-1) if n!=1 else 1
    return n

func = factorial(5)

print(func)