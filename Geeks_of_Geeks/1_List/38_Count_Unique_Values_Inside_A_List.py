"""
Count Unique Values inside a List
"""
# Method 1
print("------------Method 1 -----------------")
lst_1 = [1, 2, 2, 5, 8, 4, 4, 8]
result_1 = []

for i in lst_1:
    if i not in result_1:
        result_1.append(i)
print("No of Unique Elements in List is: {}".format(len(result_1)))

# Method 2
print("------------Method 2 -----------------")
lst_2 = [1, 2, 2, 5, 8, 4, 4, 8]
result_2 = []
count = 0

for i in lst_2:
    if i not in result_2:
        result_2.append(i)
        count += 1

print("No of Unique Elements in List is: {}".format(count))

# Method 3
print("------------Method 3 -----------------")
lst_3 = [1, 2, 2, 5, 8, 4, 4, 8]
result_3 = len(set(lst_3))
print("No of Unique Elements in List is: {}".format(result_3))



