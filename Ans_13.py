# 13. Write a Python program to generate all permutations of a given string.

from itertools import permutations

string = input()

per  = permutations(string)

list_of_per = []

for i in list(per):
    word = ''.join(map(str,i))
    list_of_per.append(word)
    
    
print(list_of_per)
