"""
Permutation of a given string

Input :  str = 'ABC'
Output : ABC
         ACB
         BAC
         BCA
         CAB
         CBA
"""
# Method 1
from itertools import permutations

str_1 = 'ABC'

result = permutations(str_1)

lst = ''
for i in list(result):
    lst += ''.join(i) + '\n'
print(lst)
