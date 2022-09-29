"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing
second character of the final pair with an underscore ('_').
"""
# Code
def solution(s):
    if len(s) % 2 != 0: # if the length of the string is odd
        s += "_"
    return [s[i:i+2] for i in range(0, len(s), 2)] # split the string into pairs of two characters
# Test 1,2,3:
print(solution('abc')) # ['ab', 'c_']
print(solution('abcdef')) # ['ab', 'cd', 'ef']
print(solution('abcdefg')) # ['ab', 'cd', 'ef', 'g_']