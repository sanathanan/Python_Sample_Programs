"""
Given a list of elements, perform grouping of similar elements, as different key-value list in dictionary.

Example:
Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}
"""

# Method 1
print("-----------Method 1 ----------")
from collections import Counter
lst_1 = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
dict_1 = Counter(lst_1)
print(dict_1)

dict_2 = {}

for i in lst_1:
    if i not in dict_2.keys():
            dict_2[i] = [i]
    else:
        dict_2[i].append(i)

print(dict_2)



