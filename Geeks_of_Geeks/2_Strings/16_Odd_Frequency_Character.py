"""
Finding Odd frequency character in a string

Example:
Input : test_str = ‘geekforgeeks’
Output : [‘r’, ‘o’, ‘f’, ‘s’]

Input : test_str = ‘g’
Output : [‘g’]
"""
from collections import Counter

# Method 1
print("------------Method 1 -------------")

test_str = 'geekforgeeks'
dict={}
for i in test_str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print("No of character count: ", dict)

lst =[]
for key, value in dict.items():
    if value %2 != 0:
        lst.append(key)
print("The odd number characters are:", lst)

# Method 2
print("------------Method 2 -------------")

test_str_2 = 'geekforgeeks'

x = set(test_str_2)

lst_2 = []
for i in x:
    if test_str_2.count(i) %2 !=0:
       lst_2.append(i)
print("The odd number characters are:", lst_2)

# Method 3
print("------------Method 3 -------------")

test_str_3 = 'ge'

lst_3 = []
for i,j in Counter(test_str_3).items():
    if j %2 !=0:
        lst_3.append(i)
print("The odd number characters are:", lst_3)
