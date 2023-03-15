"""
Consecutive Character Frequency
Example:
The original string is : geekksforgggeeks
The Consecutive characters frequency : [1, 2, 2, 1, 1, 1, 1, 3, 2, 1, 1]
"""
# Method 1
print("---------Method 1 -----------")
from itertools import groupby

str_1 = 'geekksforgggeeks'

lst_1 = []
for i,j in groupby(str_1):
   lst_1.append(len(list(j)))

print(lst_1)

# Method 2
import re
print("---------Method 2 -----------")
str_2 = 'geekksforgggeeks'
pattern = re.compile(r'(.)\1*')
result_2 = [len(i.group()) for i in re.finditer(pattern, str_2)]

print(result_2)