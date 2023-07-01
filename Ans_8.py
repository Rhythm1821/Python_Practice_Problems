# 8. Implement a function to check if a given number is prime.

def isPrime(number):
    if number>1:
        for i in range(1,number//2+1):
            if number%i==0:
                return False
            else:
                return True
            
            
func = isPrime(4)
print(func)