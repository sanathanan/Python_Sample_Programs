"""
Odd Frequency Character

Example:
Input : test_str = ‘geekforgeeks’
Output : [‘r’, ‘o’, ‘f’, ‘s’]
"""
# Method 1
from collections import Counter
print("-----------Method 1 ----------")
str_1 = 'geekforgeeks'

result = dict(Counter(str_1))

result_1 = [i for i in result if result[i] == 1]
print(result_1)