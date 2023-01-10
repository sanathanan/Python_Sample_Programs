"""
Sum of Numbers Digits in a List

Example:
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]
"""
# Method 1
print("----------Method 1 --------------")

lst_1 = [12, 67, 98, 34]
output_1 = []

for i in lst_1:
    sum = 0
    for j in str(i):
        sum += int(j)
    output_1.append(sum)
print("The Given List: ", lst_1)
print("Sum of Numbers Digits in a List: ",output_1)
