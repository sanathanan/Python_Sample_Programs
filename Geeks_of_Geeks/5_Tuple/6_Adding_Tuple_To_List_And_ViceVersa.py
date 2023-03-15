"""
Adding tuple to list and vice versa
Example:
The original list is : [5, 6, 7]
The container after addition : [5, 6, 7, 9, 10]
"""
# Method 1
print("-------Method 1 -------")
lst_1 = [5,6,7]
tuple_1 = (9,10)

for i in tuple_1:
    lst_1.append(i)

print(lst_1)

# Method 2
print("-------Method 2 -------")
lst_2 = [5,6,7]
tuple_2 = (9,10)

lst_2 += tuple_2
print(lst_2)