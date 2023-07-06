# 42. Implement a function to find the longest palindrome substring in a given string.


def longest_palindrome_substring(s):
    if not s:
        return ""

    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)
        if length > end - start:
            start, end = i - (length - 1) // 2, i + length // 2

    return s[start:end+1]


def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1

input_string = "babad"
result = longest_palindrome_substring(input_string)
print(result)