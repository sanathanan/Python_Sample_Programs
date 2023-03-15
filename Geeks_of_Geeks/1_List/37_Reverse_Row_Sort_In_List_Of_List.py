"""
Reverse Row Sort in Lists of List

Example:
The original list is : [[4, 1, 6], [7, 8], [4, 10, 8]]
The reverse sorted Matrix is : [[6, 4, 1], [8, 7], [10, 8, 4]]
"""
# Method 1
print("------Method 1 -------")
test_list_1 = [[4, 1, 6], [7, 8], [4, 10, 8]]
lst_1 = []

for i in test_list_1:
    i.sort(reverse=True)
    lst_1.append(i)

print(lst_1)

# Method 2
print("------Method 2 -------")
test_list_2 = [[4, 1, 6], [7, 8], [4, 10, 8]]

for i in test_list_2:
    i.sort(reverse=True)

print(test_list_2)

# Method 3
print("------Method 3 -------")
test_list_3 = [[4, 1, 6], [7, 8], [4, 10, 8]]
lst_3 = []
for i in test_list_3:
    lst_3.append(sorted(i, reverse=True))

print(lst_3)

# Method 3
print("------Method 4 -------")
test_list_4 = [[4, 1, 6], [7, 8], [4, 10, 8]]
lst_4 = []
for i in test_list_4:
    lst_4.append(i.sort(reverse=True))

print(test_list_4)