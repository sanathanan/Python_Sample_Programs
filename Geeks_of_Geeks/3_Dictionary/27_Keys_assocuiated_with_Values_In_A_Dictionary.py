"""
Keys associated with values in a dictionary

Example:
Input : test_dict = {‘abc’ : [10, 30], ‘bcd’ : [30, 40, 10]}
Output : {10: [‘abc’, ‘bcd’], 30: [‘abc’, ‘bcd’], 40: [‘bcd’]}
"""
# Method 1
from collections import defaultdict

dict_1 = {"abc" : [10, 30], "bcd" : [30, 40, 10]}
dict_2 = {}

res = defaultdict(list)

for i,j in dict_1.items():
    for k in j:
        res[k].append(i)

print(dict(res))
