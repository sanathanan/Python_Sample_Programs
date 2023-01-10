"""
Printing Odd Numbers in a List
Input: list2 = [12, 14, 95, 3, 73]
Output: [95, 3, 73]
"""
# Method 1
print("----------Method 1 ---------")

lst_1 = [12, 14, 95, 3, 73]
x1= []
for i in lst_1:
    if i%2 ==1:
        x1.append(i)
    else:
        pass
print(x1)

# Method 2
print("----------Method 2 ---------")

lst_2 = [12, 14, 95, 3, 73]
num = 0
x_2 = []
while num<len(lst_2):
    if lst_2[num] %2 ==1:
       x_2.append(lst_2[num])
    num+=1
print(x_2)

# Method 3
print("----------Method 3 ---------")

lst_3 = [12, 14, 95, 3, 73]
x_3 = [i for i in lst_3 if i%2 ==1]
print(x_3)