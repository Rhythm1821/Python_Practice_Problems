# 34. Implement a function to find the longest common prefix among a list of strings.

def longest_common_prefix(strs):
    if not strs:
        return ""

    min_len = min(len(s) for s in strs)
    for i in range(min_len):
        if any(strs[j][i] != strs[0][i] for j in range(1, len(strs))):
            return strs[0][:i]
    
    return strs[0][:min_len]

strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print(result)