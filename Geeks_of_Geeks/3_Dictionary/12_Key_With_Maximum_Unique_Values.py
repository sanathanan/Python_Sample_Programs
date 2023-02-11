"""
Printing key with maximum unique values

Example:
Input : test_dict = {“Gfg” : [5, 7, 9, 4, 0], “is” : [6, 7, 4, 3, 3], “Best” : [9, 9, 6, 5, 5]}
Output : “Gfg”
"""

# Method 1
print("--------Method 1 --------")
dict_1 = {'Gfg' : [5, 7, 9, 4, 0], 'is' : [6, 7, 4, 3, 3], 'Best' : [9, 9, 6, 5, 5]}

# Finding the unique values
lst = []
for i,j in dict_1.items():
    lst.append(set(j))

# Combining the count of unique values to a key in dict_1
dict_1_new = {}
for i,j in zip(list(lst), dict_1):
     dict_1_new[j] = len(i)
print('Keys having maximum unique elements: ',dict_1_new)

# Finding the maximum values from the new
max_values = max(dict_1_new.values())
max_Key = [i for i in dict_1_new if dict_1_new[i] == max_values]
print(max_Key)
