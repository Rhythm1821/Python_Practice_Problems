# 16. Implement a function to check if a given list is sorted in non-decreasing order.

def list_check(lst):
    if lst==sorted(lst):
        return "The list is sorted"
    else:
        return 'The list is not sorted'
    
func = list_check([1,24,3,4])

print(func)

