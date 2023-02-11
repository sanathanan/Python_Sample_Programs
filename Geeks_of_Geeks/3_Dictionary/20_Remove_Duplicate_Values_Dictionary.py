"""
Remove Duplicate Values Across a Dictionary

Example:
Input: test_dict = {‘Manjeet’: [1], ‘Akash’: [1, 8, 9]}
Output: {‘Manjeet’: [], ‘Akash’: [8, 9]}
"""
# Method 1
print("--------Method 1 ------------")
test_dict = {"Manjeet": [1], "Akash": [1, 8, 9]}

x=[]
for i in test_dict.keys():
    x.extend(test_dict[i])
print(x)

y=[]
for i in x:
    if (x.count(i) == 1):
        y.append(i)
print(y)


res = {}
for i in test_dict.keys():
    a = []
    for j in test_dict[i]:
        if j in y:
            a.append(j)
        res[i] = a
print(res)
