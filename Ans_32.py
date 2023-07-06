# 32. Implement a function to calculate the power of a number using recursion.

def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

base = 2
exponent = 3
result = power(base, exponent)
print(f"The result of {base} raised to the power of {exponent} is:", result)
