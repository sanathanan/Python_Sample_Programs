"""
Program to remove ith character from a string

Input : Geek
        i = 1
Output : Geek

Input : Peter
        i = 4
Output : Pete
"""
# Method 1
print("---------Method 1 --------------")
str_1 = 'geeksFORgeeks'
k = 5

res = ''
for i in range(len(str_1)):
    if i == k:
        continue
    else:
        res += ''.join(str_1[i])
print(res)

# Method 2
print("-----------Method 2 -------------------")
str_2 = 'geeksFORgeeks'
k = 5

lst_2 = list(str_2)

lst_2.pop(k)
print(''.join(lst_2))