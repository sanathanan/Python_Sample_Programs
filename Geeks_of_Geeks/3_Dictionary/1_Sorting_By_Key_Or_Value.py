import numpy as np
"""
Sorting the Keys in the dictionary
"""
dict_1 = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
print("------------Method 1---------------")
print(dict_1)
for i in sorted(dict_1.keys()):
    print(i, end=' ')

"""
Sorting the values in the dictionary
"""
dict_2 = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
print("\n", "------------Method 2---------------")
print(dict_2)
for i in sorted(dict_2.values()):
    print(i, end=' ')

"""
Sorting the dictionary (sorted by Key)
"""
dict_3 = {'ravi': '10', 'rajnish': '9','sanjeev': '15', 'yash': '2', 'suraj': '32'}
print("\n", "------------Method 3---------------")
print(dict_3)
for i in sorted(dict_3.items()):
    print(i, end='')

"""
Sorting the dictionary (sorted by Value)
"""
# dict_3a = {'ravi': '10', 'rajnish': '9','sanjeev': '15', 'yash': '2', 'suraj': '32'}
# print("\n", "------------Method 3a---------------")
# print(dict_3a)
#
# keys = list(dict_3a.keys())
# values = list(dict_3a.values())
# sorted_values = np.argsort(values)
# print(sorted_values)
# sorted_dict = {keys[i]:values[i] for i in sorted_values}
# print(sorted_dict)

"""
Sorting the keys and values in alphabetical order using the key
"""
dict_4 = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
print("\n", "------------Method 4---------------")
print(dict_4)

for i in sorted(dict_4):
    print(((i, dict_4[i])), end='')

"""
Sorting the keys and values in alphabetical order using the value
"""
# dict_5 = {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
# print("\n", "------------Method 5---------------")
# print(dict_5)
#
# for i,j in sorted(dict_5.items()):
#     for k in sorted(j):
#         print(dict_5[i], dict_5[j])