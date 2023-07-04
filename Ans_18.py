# 18. Implement a function to find the maximum subarray

def max_subarray(lst):
    max_sum = float('-inf')
    current_sum = 0
    
    for i in lst:
        current_sum+=i
        current_sum = max(i,current_sum)
        max_sum = max(max_sum,current_sum)

    return max_sum

func = max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(func)