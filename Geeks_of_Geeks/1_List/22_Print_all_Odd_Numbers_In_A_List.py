"""
Program to print all Odd Numbers in a list
Input: start = 4, end = 15
Output: 5, 7, 9, 11, 13, 15
"""

# Method 1
print("----------Method 1 ------------")
start = 4
end = 15
lst=[]
for i in range(start,end+1):
    if i%2 == 1:
        lst.append(i)
print(lst)
print(" ".join(str(x) for x in lst))