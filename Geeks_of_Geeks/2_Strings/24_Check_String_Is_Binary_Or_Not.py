"""
To check given string is binary or not.

Input: str = "01010101010"
Output: Yes

Input: str = "geeks101"
Output: No
"""
# Method 1
print("-----------Method 1 -------------")
str_1 = '01010101010'

set_str_1 = set(str_1)

temp = {'0','1'}

if temp == set_str_1 or set_str_1 == {'0'} or set_str_1 == {'1'}:
    print("Yes")
else:
    print("No")

# Method 2
print("-----------Method 2 -------------")
str_2 = '010101010102'

bny= '01'

for i in bny:
    str_2 = str_2.replace(i, '')

if len(str_2) == 0:
    print('Yes')
else:
    print('No')

# Method 3
print("-----------Method 3 -------------")
str_3 = '01010101010'

bny= '01'

for i in str_3:
    if i == '0' or i == '1':
        str_3 = str_3.replace(i, '')

if len(str_3) == 0:
    print('Yes')
else:
    print('No')