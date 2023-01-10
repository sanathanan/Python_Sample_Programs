"""
Program to find largest number in a list

Input : list1 = [10, 20, 4]
Output : 20
"""
# Method 1
print("------Method 1 -----------")
lst_1 = [10,20,4]
lst_1.sort(reverse=True)
print(lst_1[0])

# Method 2
print("------Method 2 -----------")
lst_2 = [10,20,4]
lst_2.sort()
print(lst_2[-1])

# Method 3
print("------Method 3 -----------")
lst_3 = [10,20,4]
max_element = lst_3[0]

for i in lst_3:
    if i > max_element:
        max_element = i
    elif i == max_element:
        max_element = i
print(max_element)

# Method 3
print("------Method 4 -----------")
lst_4 = [10,20,4]
max_element = lst_3[0]

print(max(lst_4))