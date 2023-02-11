"""
Counting the frequencies in a list using dictionary in python

Example:
Input : [1, 1, 1, 5, 5, 3, 1, 3, 3, 1,
              4, 4, 4, 2, 2, 2, 2]
Output : 1 : 5
         2 : 4
         3 : 3
         4 : 3
         5 : 2
"""
# Method 1
from collections import Counter
print("---------Method 1 ---------")
lst_1 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
res = Counter(lst_1)
print(res)

# Method 2
print("---------Method 2 ---------")
lst_2 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
res_2 = {}

for i in lst_2:
    if i not in res_2:
        res_2[i] = 1
    else:
        res_2[i] += 1
print(res_2)

for i,j in res_2.items():
    print('{}:{}'.format(i,j))