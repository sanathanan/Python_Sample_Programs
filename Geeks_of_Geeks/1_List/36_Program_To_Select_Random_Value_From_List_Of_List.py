"""
Program to select Random Value from List of Lists

Example:
Input : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
Output : 7
Explanation : Random number extracted from Matrix.

Input : test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]], r_no = 2
Output : 6
Explanation : Random number extracted from 2nd row from Matrix.
"""
# Method 1
import random
print("--------Method 1 ----------")
lst_1 = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

result_1 = []
for i in lst_1:
    for j in i:
        result_1.append(j)
print(result_1)
result_11 = random.choice(result_1)
print(result_11)

# Method 2
print("--------Method 2 ----------")
lst_2 = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
r_no = 2

result_2 = random.choice(lst_2[r_no])
print(result_2)