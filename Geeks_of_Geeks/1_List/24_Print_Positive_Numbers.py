"""
Program to print positive numbers in a list
Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64
"""
# Method 1
print("------------Method 1 -------------")
lst_1 = [12, -7, 5, 64, -14]
new_lst_1 = []
for i in lst_1:
    if i >= 0:
        new_lst_1.append(i)
print(', '.join(str(x) for x in new_lst_1))

# Method 2
print("------------Method 2 -------------")
lst_2 = [12, -7, 5, 64, -14]
new_lst_2 = []

i = 0
while i<len(lst_2):
    if lst_2[i] > 0:
        new_lst_2.append(lst_2[i])
    i+=1
print(', '.join(str(x) for x in new_lst_2))