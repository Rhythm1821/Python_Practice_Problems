# 19. Write a program to remove all vowels from a given string.

vowels = ['a','e','i','o','u']

def remove_vowels(string:str):
    for char in string:
        if char in vowels:
            string=string.replace(char,'')
    return string

func = remove_vowels('string')            

print(func)