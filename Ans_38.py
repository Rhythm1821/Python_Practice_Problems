# 38. Implement a function to find the missing number in a given list of consecutive numbers.

def missing_number(c_num)->list:
    missing_num = []
    start = c_num[0]
    end = c_num[-1]+1
    for num in range(start,end):
        if num not in c_num:
            missing_num.append(num)
    return missing_num
        
func = missing_number([1,2,5,6])

print(func)