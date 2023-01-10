"""
Program to Count Occurance of Elements in a list.

Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
Output: 3
Explanation: 10 appears three times in given list.
"""

# Method 1
print("-------Method 1 -----------------")
lst_1 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x1 = 10

dict_1 = {}
for i in lst_1:
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] += 1

print("The count of {} is: ".format(x1), dict_1[x1])


# Method 2
print("-------Method 2 -----------------")
lst_2 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x2 = 10

count_2 = 0
for i in lst_2:
    if i == x2:
        count_2 += 1
print("The count of {} is: ".format(x2), count_2)

# Method 3
print("-------Method 3 -----------------")
lst_3 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x3 = 10

result_3 = lst_3.count(x3)
print("The count of {} is: ".format(x3), result_3)

# Method 4
from collections import Counter

print("-------Method 4 -----------------")
lst_4 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x4 = 10

result_4 = Counter(lst_4)
print("The count of {} is: ".format(x4), result_4[x4])
