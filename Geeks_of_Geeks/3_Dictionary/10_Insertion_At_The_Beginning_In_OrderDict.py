"""
Insertion at the beginning in OrderedDict

Example:
Input:
original_dict = {'a':1, 'b':2}
item to be inserted ('c', 3)

Output:  {'c':3, 'a':1, 'b':2}
"""
# Method 1
from collections import OrderedDict
print("----------Method 1 ------------")

dict_1 = OrderedDict([('a',1,), ('b',2)])
dict_1.update({'c':3})
dict_1.move_to_end('c', last=False)
print(dict_1)

# Method 2
print("----------Method 2 ------------")
dict_2 = {'a':1, 'b':2}
dict_3 = {'c' : 3}
dict2 = list(dict_3.items()) + list(dict_2.items())
print(dict2)

