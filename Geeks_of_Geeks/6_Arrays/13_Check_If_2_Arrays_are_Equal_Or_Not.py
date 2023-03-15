"""
Check if 2 arrays are equal or not

Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not.
Two arrays are said to be equal if both of them contain same set of elements, arrangements (or permutation) of
elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.

Example:
Input:
N = 5
A[] = {1,2,5,4,0}
B[] = {2,4,5,0,1}
Output: 1
Explanation: Both the array can be
rearranged to {0,1,2,4,5}

Complete check() function which takes both the given array and their size as function arguments and returns
true if the arrays are equal else returns false.The 0 and 1 printing is done by the driver code.
"""
from collections import Counter

def check(arr1,arr2,n):

    if len(arr1) != len(arr2):
        return 0

    lst = []
    for i in arr1:
        if i in arr2:
            pass
        else:
            lst.append(i)

    for i in arr2:
        if i in arr1:
            pass
        else:
            lst.append(i)

    if len(lst)>0:
        return 0
    else:
        return 1


def check1(arr1,arr2,n):
    if Counter(arr1) == Counter(arr2):
        return 1
    else:
        return 0


# Driver Code
n=5
arr1=[1,2,2,4,0]
arr2=[2,2,2,0,4]
result = check(arr1,arr2,n)
result = check1(arr1,arr2,n)
print(result)