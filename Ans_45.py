# 45. Write a Python program to remove all duplicates from a string.

def remove_duplicates(string:str):
    new_str = ''
    for i in string:
        if i==' ':
            new_str+=i
        elif i not in new_str:
            new_str+=i
    return new_str

func = remove_duplicates('zomato paytm oyo cred tesla space x paypal')

print(func)