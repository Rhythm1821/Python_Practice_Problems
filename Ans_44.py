# 44. Implement a function to check if a given number is a perfect number.

def perfect_number(n:int):
    if type(n)==int:
        total = sum([i for i in range(1,n) if n%i==0])            
        return True if total==n else False
    else:
        raise ValueError('Argument should be int type')

perfect_number = lambda n: True if sum([i for i in range(1,n) if n%i==0])==n else False

func = perfect_number(6)
print(func)