"""
Finding size of dictionary (Finding the memory of dictionary)
"""
# Method 1
import sys
print("----------Method 1------------")
dict_1 = {"A": 1, "B": 2, "C": 3}

print("The size of the dictionary is: ",  sys.getsizeof(dict_1), "bytes")
