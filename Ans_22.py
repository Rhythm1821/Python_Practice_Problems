# 22. Implement a function to find the first non-repeating character in a string.

from collections import Counter

def first_non_repeating_char(string)->str:
    string =  string.lower()
    char_count = Counter(string)
    for char in string:
        if char_count[char]==1:
            return char
        else:
            continue
    return 'No character is non-repeating'

func = first_non_repeating_char('Amazon')

print(func)