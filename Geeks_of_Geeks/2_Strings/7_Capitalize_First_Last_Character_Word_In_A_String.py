"""
Given the string, the task is to capitalize the first and last character of each word in a string.

Input: hello world
Output: HellO WorlD
"""

input = 'hello world'
lst = input.split()

res = ''
for i in lst:
    x = i[0].upper() + i[1:-1] +i[-1].upper()
    res = res + " " + x
print(res)
