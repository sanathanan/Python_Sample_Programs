"""
Print Duplicate List of Integers

Example:
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
"""
# Method 1
from collections import Counter
print("---------Method 1 -----------")
lst_1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
lst_Duplicate_1 = []

lst_1_dict = dict(Counter(lst_1))
print(lst_1_dict)

for i,j in lst_1_dict.items():
    if j >1:
        lst_Duplicate_1.append(i)
print(lst_Duplicate_1)

# Method 2
print("---------Method 2 -----------")
lst_2 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

new_lst_2=[]
duplicate_Lst_2 =[]
for i in lst_2:
    if i not in new_lst_2:
        new_lst_2.append(i)
    else:
        duplicate_Lst_2.append(i)
print(set(duplicate_Lst_2))

# Method 3
print("---------Method 3 -----------")
lst_3 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

new_lst_3=[]
duplicate_Lst_3 =[]
for i in lst_3:
    if i not in new_lst_3:
        new_lst_3.append(i)
    elif i not in duplicate_Lst_3:
        duplicate_Lst_3.append(i)
print(duplicate_Lst_3)