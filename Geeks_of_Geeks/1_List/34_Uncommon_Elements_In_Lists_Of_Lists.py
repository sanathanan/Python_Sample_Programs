"""
Uncommon Elements in Lists of Lists

Example:
The original list 1 : [[1, 2], [3, 4], [5, 6]]
The original list 2 : [[3, 4], [5, 7], [1, 2]]
The uncommon of two lists is : [[5, 6], [5, 7]]
"""
# Method 1
print("-------Method 1 ---------")
lst_1 = [[1, 2], [3, 4], [5, 6]]
lst_11 = [[3, 4], [5, 7], [1, 2]]
result_lst_1=[]

for i in lst_1:
    if i not in lst_11:
        result_lst_1.append(i)

for i in lst_11:
    if i not in lst_1:
        result_lst_1.append(i)

print(result_lst_1)