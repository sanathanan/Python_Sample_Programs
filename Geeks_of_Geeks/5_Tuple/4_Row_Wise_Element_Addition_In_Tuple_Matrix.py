"""
Row Wise element addition in tuple matrix

Example:
test_list = [[(‘Gfg’, 3)], [(‘best’, 1)]]
cus_eles = [1, 2]
Output : [[(‘Gfg’, 3, 1)], [(‘best’, 1, 2)]]
"""
# Method 1
lst_1 = [[('Gfg', 3)], [('best', 1)]]
cus_ele_1 = [1,2]

lst_new = []
for i,j in zip(lst_1, cus_ele_1):
    for key in i:
        lst_new += (key,j)

print(lst_new)

# Method 2
lst_2 = [[('Gfg', 3)], [('best', 1)]]
cus_ele_2 = [1,2]

lst_new_2 = []

result = [[(idx, val) for idx in key] for key,  val in zip(lst_2, cus_ele_2)]
print(str(result))