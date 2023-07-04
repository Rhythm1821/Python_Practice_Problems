# 20. Implement a function to reverse the order of words in a given sentence.

def reverse_words(sentence:str):
    sentence_list = sentence.split()
    sentence_list = sentence_list[::-1]
    return ' '.join(sentence_list)

func = reverse_words('This is the python practice module')

print(func)