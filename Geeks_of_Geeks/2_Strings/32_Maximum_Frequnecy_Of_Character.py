"""
Maximum frequency of character in a string

Example:
The original string is : GeeksforGeeks
The maximum of all characters in GeeksforGeeks is : e
"""
# Method 1
from collections import Counter
print("------Method 1 ---------")

str_1 = 'GeeksforGeeks'
dict_1 = {}
for i in str_1:
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] += 1

print(dict_1)

result = [i for i in dict_1 if dict_1[i] == max(dict_1.values())]

print(result)

