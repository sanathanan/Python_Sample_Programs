"""
Maximum and Minimum K elements in a Tuple

Example:
Input : test_tup = (3, 7, 1, 18, 9), k = 2
Output : (3, 1, 9, 18)
"""
# Method 1
print("----------Method 1 ---------")
lst_1 = (3, 7, 1, 18, 9)
k1 = 2
sort_lst1 = sorted(lst_1)
print(sort_lst1)
result_1 = sort_lst1[:k1] + sort_lst1[-k1:]
print(result_1)
