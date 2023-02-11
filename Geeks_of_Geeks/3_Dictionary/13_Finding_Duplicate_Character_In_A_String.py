"""
Given a string, find all the duplicate characters which are similar to each other. Let us look at the example.

Example:
Input : hello
Output : l

Example:
Input : geeksforgeeeks
Output : e g k s
"""

# Method 1
print("Method 1")
str_1 = 'geeksforgeeeks'
dict_1 = {}

for i in str_1:
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] += 1
print(dict_1)

result = [i for i,j in dict_1.items() if j>1]
print(result)

# Method 2
from collections import Counter
print("Method 2")
str_2 = 'geeksforgeeeks'

dict_2 = Counter(str_2)
print(dict_2)

for i,j in dict_2.items():
    if j > 1:
        print(i)
