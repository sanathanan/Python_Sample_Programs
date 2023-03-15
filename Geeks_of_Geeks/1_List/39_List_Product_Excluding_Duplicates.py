"""
List Product excluding duplicates

Example:
The original list is : [1, 3, 5, 6, 3, 5, 6, 1]
Duplication removal list product : 90
"""
# Method 1
print("---------Method 1 ----------")
lst_1 = [1, 3, 5, 6, 3, 5, 6, 1]
new_lst_1 = list(set(lst_1))
print(new_lst_1)
result_1 = 1
for i in new_lst_1:
    result_1 = (result_1*i)
print(result_1)

# Method 2
print("---------Method 2 ----------")
lst_2 = [1, 3, 5, 6, 3, 5, 6, 1]
new_lst_2 = list(set(lst_2))
print(new_lst_2)
result_2 = 1
for i in new_lst_2:
    result_2 *= i
print(result_2)