"""
Sum of Array

Given an integer array Arr[] of size N. The task is to find sum of it.

Example:
N = 4
Arr[] = {1, 2, 3, 4}
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.
"""

def _sum(arr,n):
    result = sum(arr)
    return result

# Driver Code
n=4
arr= [1,2,3,4]
result = _sum(arr,n)
print(result)