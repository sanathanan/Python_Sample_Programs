"""
Reverse all string in list

Example:
The original list is : ['geeks', 'for', 'geeks', 'is', 'best']
The reversed string list is : ['skeeg', 'rof', 'skeeg', 'si', 'tseb']
"""
# Method 1
print("------Method 1 ---------")
lst_1 = ['geeks', 'for', 'geeks', 'is', 'best']
result = []
for i in lst_1:
    result.append(sorted(i, reverse=True))
print(result)

lst_1_new = []
for i in result:
    lst_1_new.append(''.join(i))
print(lst_1_new)

# Method 2
print("------Method 2 ---------")
lst_2 = ['geeks', 'for', 'geeks', 'is', 'best']

result_2 = [i[::-1] for i in lst_2]
print(result_2)

# Method 2
print("------Method 3 ---------")
lst_3 = ['geeks', 'for', 'geeks', 'is', 'best']

result_3 = [''.join(reversed(i)) for i in lst_3]
print(result_3)