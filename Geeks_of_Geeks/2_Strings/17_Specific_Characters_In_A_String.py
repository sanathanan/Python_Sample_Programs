"""
Specific Characters frequency in String List

input : test_list = [“geeksforgeeks is best for geeks”],

chr_list = [‘e’, ‘b’, ‘g’, ‘f’]

Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 2}
"""
from collections import Counter

# Method 1
print("------------Method 1 ----------------")
test_list = ["geeksforgeeks is best for geeks"]
chr_list = ['e', 'b', 'g', 'f']

# Converting list to string
str_list = ''.join(test_list)
# Removing empty characters from string
str_list = str_list.replace(' ', '')
# creating empty dictionary
dict_1 = {}

for i in str_list:
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1

print("The count of each clement in given string: ", dict_1)

# Creating dictionary to store the results
char_dict = {}
for i in chr_list:
    char_dict[i] = dict_1[i]
print(char_dict)

# Method 2:
print("------------Method 2 ----------------")
test_list_2 = ["geeksforgeeks is best for geeks"]
chr_list_2 = ['e', 'b', 'g', 'f']
# Converting list to string
str_list_2 = ''.join(test_list_2)
# Removing empty characters from string
str_list_2 = str_list_2.replace(' ', '')
res_2 = dict(Counter(str_list_2))
print("The count of each clement in given string: ", res_2)

result_2 = {i:j for i,j in res_2.items() if i in chr_list_2}
print(result_2)

#  Method 3
print("------------Method 3 ----------------")
test_list_3 = ["geeksforgeeks is best for geeks"]
chr_list_3 = ['e', 'b', 'g', 'f']

dict_3 = {}

for i in chr_list_3:
    dict_3[i] = test_list_3[0].count(i)
print(dict_3)