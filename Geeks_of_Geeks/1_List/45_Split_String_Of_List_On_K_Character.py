"""
Split String of List on K character

Example:
The original list is : ['Gfg is best', 'for Geeks', 'Preparing']
The extended list after split strings : ['Gfg', 'is', 'best', 'for', 'Geeks', 'Preparing']
"""
# Method 1
print("--------Method 1 -------")
lst_1 = ['Gfg is best', 'for Geeks', 'Preparing']
result_1 = []

k = ' '

for i in lst_1:
    result_1.extend(i.split(k))

print(result_1)

