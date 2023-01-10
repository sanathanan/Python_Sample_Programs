"""
Program to print even numbers in a range

Input: start = 4, end = 15
Output: 4, 6, 8, 10, 12, 14
"""
# Method 1
print("----------Method 1 ------------")

start = 4
end = 15
lst_1 = []
for i in range(start, end+1):
    if i%2 == 0:
        lst_1.append(i)
print(" ".join(str(x) for x in lst_1))