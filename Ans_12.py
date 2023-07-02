# 12. Implement a function to check if a given string is an anagram of another string.

def anagram(str1,str2)->str:
    # Check if str2 is an anagram of str1
    if sorted(str1)==sorted(str2):
        return 'Both strings are anagram'
    else:
        return 'Both strings are not anagrams'

func = anagram('silent','listen')

print(func)