"""
Program to multiply all elements in a list

Input :  list1 = [1, 2, 3]
Output : 6
Explanation: 1*2*3=6
"""

# Method 1
import numpy

print("------------Method 1 ----------")
result = 1
lst_1 = [1, 2, 3]
for i in lst_1:
    result = result*i
print(result)

# Method 2
import numpy as np
print("------------Method 2 ----------")
lst_2 = [1, 2, 3]
print(numpy.prod(lst_2))

# Method 3
import math
print("------------Method 3 ----------")
lst_3 = [1, 2, 3]
print(math.prod(lst_3))

# Method 4
from functools import reduce
print("------------Method 4 ----------")
lst_4 = [1, 2, 3]
result_4 = reduce((lambda x,y : x*y), lst_4)
print(result_4)
