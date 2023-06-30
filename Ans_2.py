# 2. Implement a function to check if a given string is a palindrome.

def palindrome(string):
    string = string.lower()
    if string==string[::-1]:
        return 'The string is a palindrome'
    else:
        return 'The string is not a palindrome'

func = palindrome('MALAYALaM')

print(func)