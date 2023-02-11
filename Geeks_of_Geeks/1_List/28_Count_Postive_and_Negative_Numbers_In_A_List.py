"""
Program to count Positive and Negative Numbers in a list
Input: list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3
"""
# Method 1
lst_1 = [2, -7, 5, -64, -14]
pos = 0
neg = 0
for i in lst_1:
    if i >=0:
        pos+=1
    else:
        neg+=1
print("Positive number count: ", pos)
print("Negative number count: ", neg)
