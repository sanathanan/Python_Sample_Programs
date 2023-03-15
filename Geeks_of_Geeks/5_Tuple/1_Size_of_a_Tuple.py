"""
Finding size of Tuple
"""
# Method 1
print("---------Method 1 -----------")
Tuple1 = ("A", 1, "B", 2, "C", 3)

print(Tuple1.__sizeof__(),  'bytes')

# Method 2
import sys
print("---------Method 2 -----------")
Tuple2 = ("A", 1, "B", 2, "C", 3)

print(sys.getsizeof(Tuple2), 'bytes')