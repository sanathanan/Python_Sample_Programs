"""
Remove Empty List from List

Example:
The original list is : [5, 6, [], 3, [], [], 9]
List after empty list removal : [5, 6, 3, 9]
"""
# Method 1
print("-----------Method 1 ------------")
lst_1 = [5, 6, [], 3, [], [], 9]
new_lst_1 = []

for i in lst_1:
    if i:
        new_lst_1.append(i)
print(new_lst_1)

# Method 2
print("-----------Method 2 ------------")
lst_2 = [5, 6, [], 3, [], [], 9]
new_lst_2 = [i for i in lst_2 if i]
print(new_lst_2)

# Method 3
print("-----------Method 3 ------------")
lst_3 = [5, 6, [], 3, [], [], 9]
new_lst_3 = filter(None, lst_3)
print(list(new_lst_3))

# Method 3=4
print("-----------Method 4 ------------")
lst_4 = [5, 6, [], 3, [], [], 9]
new_lst_4= []
for i,j in enumerate(lst_4):
    if j != []:
        new_lst_4.append(j)
print(new_lst_4)