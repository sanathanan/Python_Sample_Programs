"""
Merging Two Dictionaries
"""
# Method 1
print("----------Method 1 ----------")
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

for i in dict1:
    dict2[i] = dict1[i]
print(dict2)

# Method 2
print("----------Method 2 ----------")
dict11 = {'a': 10, 'b': 8}
dict22 = {'d': 6, 'c': 4}

result_2 = {**dict11, **dict22}
print(result_2)

# Method 3
print("----------Method 3 ----------")
dict10 = {'a': 10, 'b': 8}
dict20 = {'d': 6, 'c': 4}

result_3 = dict10 | dict20
print(result_3)