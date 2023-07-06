# 40. Implement a function to check if a given string is a valid palindrome considering case sensitivity.

palindrome_check = lambda string: True if string==string[::-1] else False

func = palindrome_check('Malayalam')

print(func)