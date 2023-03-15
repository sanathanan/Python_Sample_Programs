"""
Convert List of List to Dictionary

Example:
The original list is : [[‘a’, ‘b’, 1, 2], [‘c’, ‘d’, 3, 4], [‘e’, ‘f’, 5, 6]]
The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}
"""
# Method 1
print("---------Method 1 ------------")
lst_1 = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
dict={}
for i in lst_1:
    dict[tuple(i[:2])] = tuple(i[2:])

print(dict)