"""
Given an array Arr of size N, swap the Kth element from beginning with Kth element from end.

Example:
N = 8, K = 3, Arr[] = {1, 2, 3, 4, 5, 6, 7, 8}
Output: 1 2 6 4 5 3 7 8
Explanation: Kth element from beginning is 3 and from end is 6.
"""

def swapKth(arr,n,k):
    first_pos= arr[k-1]
    arr[k-1] = arr[-k]
    arr[-k] = first_pos

    return arr

# Driver Code
n=8
arr= [1, 2, 3, 4, 5, 6, 7, 8]
k=3
result = swapKth(arr,n,k)
print(result)