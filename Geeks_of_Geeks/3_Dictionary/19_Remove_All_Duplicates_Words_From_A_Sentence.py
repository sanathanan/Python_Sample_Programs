"""
Remove all duplicates words from a given sentence

Example:
Input : Geeks for Geeks
Output : Geeks for
"""
# Method 1
print("----------Method 1 -----------")
input_1 = 'Geeks for Geeks'
lst= []
for i in input_1.split():
    if i not in lst:
        lst.append(i)
    else:
        pass
res = ' '.join(lst)
print(res)

# Method 2
print("----------Method 2 -----------")
input_2 = 'Geeks for Geeks'
lst_2=[]
res2 = ' '.join(set([i for i in input_2.split()]))
print(res2)

# Method 3
from collections import Counter
print("----------Method 3 -----------")
input_3 = 'Geeks for Geeks'

res_3 = Counter(input_3.split())
print(' '.join(res_3.keys()))
