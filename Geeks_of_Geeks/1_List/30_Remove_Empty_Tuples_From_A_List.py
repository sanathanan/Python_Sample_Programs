"""
Remove Empty Tuples from a List

Exanple:
Input : tuples = [(), (‘ram’,’15’,’8′), (), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”,”),()]
Output : [(‘ram’, ’15’, ‘8’), (‘laxman’, ‘sita’), (‘krishna’, ‘akbar’, ’45’), (”, ”)]
"""
# Method 1
print("--------------Method 1 -----------")
lst_1 =[(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),()]
lst_new = []
for i in lst_1:
    if len(i) != 0:
        lst_new.append(i)
print(lst_new)

# Method 2
print("--------------Method 2 -----------")
lst_2 =[(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),()]

lst_new_2 = [i for i in lst_2 if i]
print(lst_new_2)

# Method 3
print("--------------Method 3 -----------")
lst_3 =[(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","),()]

lst_new_3 = filter(None, lst_3)
print(list(lst_new_3))


