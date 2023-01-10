"""
Printing Even Numbers in a List
Input: list1 = [2, 7, 5, 64, 14]
Output: [2, 64, 14]
"""
# Method 1
print("----------Method 1 ---------")

lst_1 = [2, 7, 5, 64, 14]
x1= []
for i in lst_1:
    if i%2 ==0:
        x1.append(i)
    else:
        pass
print(x1)

# Method 2
print("----------Method 2 ---------")

lst_2 = [2, 7, 5, 64, 14]
num = 0
x_2 = []
while num<len(lst_2):
    if lst_2[num] %2 ==0:
       x_2.append(lst_2[num])
    num+=1
print(x_2)

# Method 3
print("----------Method 3 ---------")

lst_3 = [2, 7, 5, 64, 14]
x_3 = [i for i in lst_3 if i%2 ==0]
print(x_3)