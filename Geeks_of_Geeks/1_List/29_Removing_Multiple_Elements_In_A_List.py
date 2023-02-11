"""
Program to remove multiple element in a list
Input: [12, 15, 3, 10]
Output: Remove = [12, 3], New_List = [15, 10]
"""
# Method 1
print("-----Method 1 -------")
lst_1 = [12, 15, 3, 10]
remove_1 = [12, 3]
new_lst_1 = []
for i in lst_1:
    if i not in remove_1:
        new_lst_1.append(i)
print(new_lst_1)