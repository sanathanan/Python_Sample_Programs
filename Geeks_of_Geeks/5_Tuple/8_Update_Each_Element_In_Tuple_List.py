"""
Update each element in tuple list

Example:
test_list = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
add_ele = 4
List after bulk update : [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
"""
# Method 1
print("--------Method 1 ---------")
test_list_1 = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
add_ele_1 = 4

res = [tuple(j+add_ele_1 for j in i) for i in test_list_1]

print(res)