"""
Given an array Arr of N positive integers. Your task is to find the elements whose value is equal to that
of its index value ( Consider 1-based indexing ).

Note: There can be more than one element in the array which have the same value as its index.
You need to include every such element's index. Follows 1-based indexing of the array

Your Task:
You don't need to read input or print anything. Your task is to complete the function valueEqualToIndex()
which takes the array of integers arr[] and n as parameters and returns an array of indices where the
given conditions are satisfied. When there is no such element exists then return an empty array of length 0.

Example:
Input:
N = 5
Arr[] = {15, 2, 45, 12, 7}
Output: 2
Explanation: Only Arr[2] = 2 exists here.
"""

def valueEqualToIndex(arr, n):

    dict = {}
    for i, j in enumerate(arr):
        dict[i+1] = j

    lst = []
    for i, j in dict.items():
        if i == j:
            lst.append(i)
        else:
            pass

    return lst



# Driver Code
n = 5
arr = [15, 21, 45, 41, 7]
result = valueEqualToIndex(arr, n)
print(result)

# dict = {}
# for i,j in enumerate(result):
#     dict[i+1] = j
#
# print(dict)
#
# lst = []
# for i, j in dict.items():
#     if i == j:
#         lst.append(i)
#     else:
#         pass
#
# print(lst)
#
# if len(lst) > 0:
#     print(lst)
# else:
#     print(0)

