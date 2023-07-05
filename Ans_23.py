# 23. Write a program to find the prime factors of a given number.


def prime_factor(n:int):
    factors = []
    i=2

    while i<=n:
        if n % i==0:
            factors.append(i)
            n//=i
        else:
            i += 1
    return factors




func = prime_factor(12)
print(func)