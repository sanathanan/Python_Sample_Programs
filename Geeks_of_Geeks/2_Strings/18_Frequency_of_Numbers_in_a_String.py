"""
Frequency of Numbers in a given string
"""
import re
# Method 1
print('----------Method 1 ---------------------')
test_str_1 = "geeks4feeks is No. 1 4 geeks 456"
count = 0
for i in test_str_1:
    if i.isdigit():
        count += 1
    else:
        pass
print("The number of integers present in given string: ", count)

# Method 2
print('----------Method 2 ---------------------')
test_str_2 = "geeks4feeks is No. 1 4 geeks 456"

num = '1234567890'

res_2 = 0
for i in test_str_2:
    if i in num:
        res_2  += 1
print("The number of integers present in given string: ", res_2)

# Method 3
print('----------Method 3 ---------------------')
test_str_3 = "geeks4feeks is No. 1 4 geeks 4 5 6"


res_3 = len(re.findall(r'\d+', test_str_3))
print("The number of integers present in given string: ", res_3)