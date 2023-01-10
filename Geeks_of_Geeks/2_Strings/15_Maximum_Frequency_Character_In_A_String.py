"""
Finding the maximum frequency character in a string
"""
from collections import Counter

# Method 1
print("-----------Method 1--------------")
test_str = "GeeksforGeeks"
dict = {}

for i in test_str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print("The maximum character count: ", dict)
max_char = max(dict, key=dict.get)
print(max_char)

# Method 2
print("-----------Method 2--------------")
test_str_2 = "GeeksforGeeks"

res_2 = Counter(test_str_2)

max_char_2 = max(res_2, key=res_2.get)
print(max_char_2)