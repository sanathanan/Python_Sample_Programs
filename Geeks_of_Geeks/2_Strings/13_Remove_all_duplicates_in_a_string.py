"""
Remove all duplicates from a given string in Python

Example:
Input : geeksforgeeks
Output : geksfor
"""
from collections import OrderedDict

# Method 1 - Without order
print("------------Method 1 -------------")
str1 = 'geeksforgeeks'
print(''.join(set(str1)))

# Method 2 - With order
print("------------Method 2 -------------")
str2 = 'geeksforgeeks'
str = ''

for i in str2:
    if i in str:
        pass
    else:
        str = str+i
print(str)

# Method 3 - With order
print("------------Method 3 -------------")
str3 = 'geeksforgeeks'

# OrderDict is a dictionary, that will remember the order of the keys that were inserted first.
print(''.join(OrderedDict.fromkeys(str3)))