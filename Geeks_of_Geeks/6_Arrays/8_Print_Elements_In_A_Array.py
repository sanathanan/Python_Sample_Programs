"""
Printing Elements in a array

Given an array Arr of size N, print all its elements.

Example:
Input:
N = 5
Arr[] = {1, 2, 3, 4, 5}
Output: 1 2 3 4 5
"""

def print_Array(arr,n):

    str_ = ''
    for i in arr:
        str_ += (str(i) + ' ')
    return str_


# Driver Code
n=5
arr=[1,2,3,4,5]
result = print_Array(arr,n)
print(result)