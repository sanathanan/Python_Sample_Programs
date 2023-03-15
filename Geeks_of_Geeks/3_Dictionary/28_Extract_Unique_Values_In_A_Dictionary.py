"""
Extract Unique Values in a dictionary

Example:
The original dictionary is : {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
The unique values list is : [1, 2, 5, 6, 7, 8, 10, 11, 12]
"""

# Method 1
print("--------Method 1 ------------")
dict_1 = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
lst_1 = []
for key,val in dict_1.items():
    for i in val:
        if i not in lst_1:
            lst_1.append(i)
        else:
            continue

print(lst_1)

# Method 2
print("--------Method 2 ------------")
dict_2 = {'gfg': [5, 6, 7, 8], 'is': [10, 11, 7, 5], 'best': [6, 12, 10, 8], 'for': [1, 2, 5]}
result_2 = set({j for i in dict_2.values() for j in i})
print(result_2)