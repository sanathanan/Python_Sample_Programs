"""
Finding sum of all items in the dictionary

Input : {‘a’: 100, ‘b’:200, ‘c’:300}
Output : 600
"""
# Method 1
print("-----------Method 1 --------")
dict_1 = {'a':100, 'b':200, 'c':300}

dict_1_sum = 0
for i in dict_1:
    dict_1_sum += dict_1[i]
print(dict_1_sum)

# Method 2
print("-----------Method 2 --------")
dict_2 = {'a':100, 'b':200, 'c':300}
dict_2_Values = sum(dict_2.values())
print(dict_2_Values)

# Method 3
print("-----------Method 3 --------")
dict_3 = {'a':100, 'b':200, 'c':300}
dict_2_Values = sum(dict_3[i] for i in dict_3)
print(dict_2_Values)