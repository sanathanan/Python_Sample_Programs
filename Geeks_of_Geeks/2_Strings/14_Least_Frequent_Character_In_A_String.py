"""
Least frequent character in string
"""
from collections import Counter
# Method 1
print("-------------Method 1 -----------------")
str = "GeeksforGeeks"

dict = {}

for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print("Each letter count: ",dict)

min_char = min(dict, key= dict.get)
print(min_char)

# Method 2
print("-------------Method 2 -----------------")
str_2 = "GeeksforGeeks"

res_2 = Counter(str_2)
min_char_2 = min(res_2, key=res_2.get)

print(min_char_2)
