"""
Modulo of tuple elements

Example:
The original tuple 1 : (10, 4, 5, 6)
The original tuple 2 : (5, 6, 7, 5)
The modulus tuple : (0, 4, 5, 1)
"""
# Method 1
print("---------Method 1 -----------")
tuple_1 = (10, 4, 5, 6)
tuple_2 = (5, 6, 7, 5)

res = []
for i, j in zip(tuple_1, tuple_2):
    res.append(i%j)

print(tuple(res))

# Method 2
print("---------Method 2 -----------")
tuple_11 = (10, 4, 5, 6)
tuple_22 = (5, 6, 7, 5)

res_2 = ((i%j) for i,j in zip(tuple_11, tuple_22))
print(tuple(res_2))