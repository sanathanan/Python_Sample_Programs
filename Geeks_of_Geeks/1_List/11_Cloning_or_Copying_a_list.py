"""
Cloning or Copying a List
"""
import copy

# Method 1
lst_1 = [1,2,3,4,5]
new_lst_1 = lst_1[:]
print("-------------Method 1 -----------------")
print("Given List: ", lst_1)
print("Copied List: ", new_lst_1)

# Method 2
lst_2 = [1,2,3,4,5]
new_lst_2 = []
for i in lst_2:
    new_lst_2.append(i)
print("-------------Method 2 -----------------")
print("Given List: ", lst_2)
print("Copied List: ", new_lst_2)


# Method 3
lst_3 = [1,2,3,4,5]
new_lst_3 = []
new_lst_3.extend(lst_3)
print("-------------Method 3 -----------------")
print("Given List: ", lst_3)
print("Copied List: ", new_lst_3)

# Method 4
lst_4 = [1,2,3,4,5]
new_lst_4 = lst_4
print("-------------Method 4 -----------------")
print("Given List: ", lst_4)
print("Copied List: ", new_lst_4)

# Method 5 (Shallow Copy)
lst_5 = [1,2,3,4,5]
new_lst_5 = copy.copy(lst_5)
print("-------------Method 5 -----------------")
print("Given List: ", lst_5)
print("Copied List: ", new_lst_5)

# Method 6 (List Comprehension)
lst_6 = [1,2,3,4,5]
new_lst_6 = [i for i in lst_5]
print("-------------Method 6 -----------------")
print("Given List: ", lst_6)
print("Copied List: ", new_lst_6)

# Method 7 (Deep Copy)
lst_7 = [1,2,3,4,5]
new_lst_7 = copy.deepcopy(lst_7)
print("-------------Method 7 -----------------")
print("Given List: ", lst_7)
print("Copied List: ", new_lst_7)