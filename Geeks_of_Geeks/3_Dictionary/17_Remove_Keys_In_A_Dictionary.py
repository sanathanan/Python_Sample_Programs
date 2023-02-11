"""
Remove Keys in a Dictionary
"""
# Method 1
print("-----------Method 1 ----------------")
dict1 =   {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}

del dict1['Mani']

print(dict1)

# Method 2
print("-----------Method 2 ----------------")
dict2 =   {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}

result_2 = dict2.pop('Mani')
print(dict2)

# Method 2a
print("-----------Method 2a ----------------")
dict2a =   {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22}

result_2 = dict2a.pop('Mani', 'No Key Found')
print(dict2a)

# Method 3
print("-----------Method 3 ----------------")
dict3 =   {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}

dict_3 = {}
for i,j in dict3.items():
    if i == 'Mani':
        pass
    else:
        dict_3[i] = j
print(dict_3)

