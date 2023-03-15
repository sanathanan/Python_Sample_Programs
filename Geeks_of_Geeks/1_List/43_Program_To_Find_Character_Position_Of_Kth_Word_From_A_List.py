"""
Program to find character position of Kth word from a list

Example:
Input : test_list = [“geekforgeeks”, “is”, “best”, “for”, “geeks”], K = 21
Output : 0
21st index occurs in “geeks” and point to “g” which is 0th element of word.
"""

# Method 1
print("---------Method 1 -------")
lst_1 = ["geekforgeeks", "is", "best", "for", "geeks"]
k = 21
lst = []
for i in lst_1:
    for j in enumerate(i):
        lst.append(j)
print(lst[k][0])

