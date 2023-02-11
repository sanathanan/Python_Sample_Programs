"""
Program to print all positive numbers in a given range.

Input: start = -4, end = 5
Output: 0, 1, 2, 3, 4, 5
"""
# Method 1
print("-------Method 1 ------------")
start = -4
end = 5
lst_1 = []
for i in range(start, end+1):
    if i >= 0:
        lst_1.append(i)
print(", ".join(str(x) for x in lst_1))

# Method 2
print("-------Method 2 ------------")
start_2 = -4
end_2 = 5
lst_2 = []
while start_2 < end_2+1:
    if start_2 >= 0:
        lst_2.append(start_2)
    start_2 += 1
print(lst_2)