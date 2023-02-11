"""
Program to print Negative numbers in a list
Input: list1 = [12, -7, 5, 64, -14]
Output: -7, -14
"""
# Method 1
print("----------Meyhod 1-----------")
lst_1 = [12, -7, 5, 64, -14]
neg=[]
for i in lst_1:
    if i < 0:
        neg.append(i)
print(neg)

# Method 2
print("----------Method 2-----------")
lst_2 = [12, -7, 5, 64, -14]
neg_2=[]
i = 0

while i < len(lst_2):
    if lst_2[i] < 0:
        neg_2.append(lst_2[i])
    i+=1
print(neg_2)