# 24. Implement a function to check if a given number is a power of two.

def is_power_of_two(n):
    if n <= 0:
        return False
    return n & (n - 1) == 0


func = is_power_of_two(89)
print(func)