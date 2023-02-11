"""
Program to print all Negative Numbers in a given range
Input: a = -4, b = 5
Output: -4, -3, -2, -1
"""
# Method 1
print("--------Method 1--------")
start = -4
end = 5
lst_1 = []
for i in range(start, end+1):
    if i < 0:
        lst_1.append(i)
print(lst_1)

# Method 2
print("---------Method 2 ---------")
a = -4
b = 5

lst_2 = []

while a< b+1:
    if a < 0:
        lst_2.append(a)
    a+=1
print(lst_2)