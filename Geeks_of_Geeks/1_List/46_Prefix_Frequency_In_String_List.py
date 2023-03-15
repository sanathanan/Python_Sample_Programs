"""
Prefix frequency in string list

Example:
The original list is : ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']
k= 'gfg
Strings count with matching frequency : 3
"""
# Method 1
print("-------Method 1 ------")

lst_1 = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']

count = 0
k = 'gfg'
for i in lst_1:
    if k in i:
        count+=1
    else:
        count+=0

print(count)

# Method 2
import re
print("-------Method 2 ------")

lst_2 = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses']

count_2 = 0

pattern = re.compile('^gfg')
for i in lst_2:
    if re.match(pattern,i):
        count_2 += 1

print(count_2)