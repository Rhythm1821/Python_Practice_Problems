# 21. Write a Python program to check if two strings are anagrams of each other.

def anagram(string1,string2)->str:
    if sorted(string1)==sorted(string2):
        return True
    else:
        return False

func = anagram('silent','listen')

print(func)