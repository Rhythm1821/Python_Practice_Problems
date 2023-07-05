# 27. Write a program to find the greatest common divisor (GCD) of two numbers.


def greatest_common_divisor(n1,n2):
    gcd=0
    for i in range(1,n1//2+1):
        if n1%i==0 and n2%i==0:
            gcd = i if i>gcd else gcd 
    
    return gcd

func = greatest_common_divisor(56,80)
print(func)