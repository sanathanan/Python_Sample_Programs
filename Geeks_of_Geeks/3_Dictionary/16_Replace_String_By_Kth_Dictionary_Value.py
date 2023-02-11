"""
Replace String by Kth Dictionary value

Example:
Input : test_list = [“Gfg”, “is”, “Best”],
subs_dict = {“Gfg” : [5, 6, 7], “is” : [7, 4, 2]},
K = 0 Output : [5, 7, “Best”]
Explanation : “Gfg” and “is” is replaced by 5, 7 as 0th index in dictionary value list.
"""
# Method 1
print("-------------Method 1 ----------------")
lst_1 = ["Gfg", "is", "Best"]
sub_dict_1 = {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}
k = 0

lst = []

for i in lst_1:
    if i in sub_dict_1.keys():
        lst.append(sub_dict_1[i][k])
    else:
        lst.append(i)

print(lst)

# Method 2
print("-------------Method 2 ----------------")
lst_2 = ["Gfg", "is", "Best"]
sub_dict_2 = {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}
k = 0

lst2= []
for i in lst_2:
   lst2.append(sub_dict_2.get(i,i))

# print(lst2)

res = []
for i in lst2:
    # print(i)
    if i in sub_dict_2.values():
        res.append(i[k])
    else:
        res.append(i)

print(res)
