# 29. Write a Python program to check if a given string is a valid palindrome ignoring 
#non-alphanumeric characters.

def is_valid_palindrome(sentece):
    new_sentence = ''
    for i in sentece:
        if i.isalnum():
            new_sentence+=i
    return True if new_sentence==new_sentence[::-1] else False

func = is_valid_palindrome("A man, a plan, a canal: Panama")
print(func)