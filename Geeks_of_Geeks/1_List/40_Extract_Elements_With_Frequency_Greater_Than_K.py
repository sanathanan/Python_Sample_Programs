"""
Extract elements with frequency greater than k

Example:
Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
Output : [4, 3]
"""
# Method 1
print("----------Method 1 ----------")
from collections import Counter
lst_1 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k1 = 3

lst = dict(Counter(lst_1))
result_1 = []
for i in lst:
    if lst[i] > k1:
        result_1.append(i)

print(result_1)

# Method 2
print("----------Method 2 ----------")
lst_2 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k2 = 3
result_2  = []
for i in lst_2:
    result = lst_2.count(i)
    if result > k2:
        result_2.append(i)
print(list(set(result_2)))