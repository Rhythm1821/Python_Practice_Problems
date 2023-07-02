# 14. Implement a function to calculate the Fibonacci sequence up to a given number of terms.

def fibonacci(n):
    num1 = 0
    num2 = 1

    for i in range(n):
        num = num1 + num2
        num1 = num2
        num2 = num
        
    return num

func = fibonacci(7)

print(func)