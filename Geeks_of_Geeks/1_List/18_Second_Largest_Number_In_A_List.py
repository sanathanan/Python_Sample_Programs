"""
Program to find the second largest number in a list

Input: list2 = [70, 11, 20, 4, 100]
Output: 70
"""
# Method 1
print("------------Method 1 ------------")
lst_1 = [70, 11, 20, 4, 100]
lst_1 = list(set(lst_1))
lst_1.sort()
print(lst_1[-2])

# Method 2
print("------------Method 2 ------------")
lst_2 = [70, 11, 20, 4, 100, 100, 70, 71]
lst_2 = list(set(lst_2))
max_element = max(lst_2)
x_2 = []
for i in lst_2:
    if i < max_element:
       x_2.append(i)
x_2.sort()
print(x_2[-1])
