# 37. Write a Python program to reverse the order of words 
# in a sentence while preserving the word order.


reverse = lambda x: ' '.join(x.split()[::-1])

func = reverse('My name is Rhythm Rawat')

print(func)

