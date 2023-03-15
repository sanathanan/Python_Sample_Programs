"""
Sum of Tuple Elements

Example:
The original tuple is : (7, 8, 9, 1, 10, 7)
The summation of tuple elements are : 42
"""
# Method 1
print("------Method 1 -------")
tuple1 = (7, 8, 9, 1, 10, 7)

print(sum(tuple1))

# Method 2
print("------Method 2 -------")
tuple2 = (7, 8, 9, 1, 10, 7)

count_2 = 0
for i in tuple2:
    count_2 += i

print(count_2)