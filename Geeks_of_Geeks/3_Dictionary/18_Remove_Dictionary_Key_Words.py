"""
Remove Dictionary Key Words

Example:
Input = "gfg is best for geeks"; test_dict = {'geeks' : 1, 'best': 6}
Output = "gfg is  for"
"""
# Method 1
print("---------Method 1 ------------")
str_1 = "gfg is best for geeks"
test_dict_1 = {'geeks' : 1, 'best': 6}
res = []
temp= ''
for i in str_1.split():
    if i not in test_dict_1.keys():
       res.append(i)
print(res)
temp = ' '.join(res)
print(temp)

# Method 2
print("---------Method 2 ------------")
str_2 = "gfg is best for geeks"
test_dict_2 = {'geeks' : 1, 'best': 6}

res_2 = ' '.join([i for i in str_2.split() if i not in test_dict_2.keys()])
print(res_2)
# temp2 = ' '.join(res_2)
# print(temp2)
