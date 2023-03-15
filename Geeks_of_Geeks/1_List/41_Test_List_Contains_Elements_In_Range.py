"""
Testing List contains elements in range


Example:
The original list is : [4, 5, 6, 7, 3, 9], i,j = 3,10
Does list contain all elements in range : True
"""
# Method 1
print("--------Method 1 ---------")
lst1 = [4, 5, 6, 7, 3, 9]
i,j = 3,10

result_1 = []
for i in lst1:
    if i >=3 and i<10:
        result_1.append(i)
print(result_1)

if result_1 == lst1 :
    print("True")
else:
    print("False")

# Method 2
print("--------Method 2 ---------")
lst2 = [4, 5, 6, 7, 3, 9]
i2,j2 = 3,10

res= True
for i in lst2:
    if i<i2 or i >=j2:
        res = False
        break
print(res)