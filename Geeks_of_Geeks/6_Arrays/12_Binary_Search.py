"""
Binary Search
Given a sorted array of size N and an integer K, find the position at which K is present
in the array using binary search.

You dont need to read input or print anything. Complete the function binarysearch() which takes arr[],
N and K as input parameters and returns the index of K in the array. If K is not present in the array, return -1.

Example:
Input:
N = 5
arr[] = {1 2 3 4 5}
K = 4
Output: 3
Explanation: 4 appears at index 3.
"""
def binary_Search(arr,n,k):

    num = n//2
    first_pos = arr[:num]
    last_pos = arr[num:]

    result = ''
    if k in first_pos:
        for idx, j in enumerate(first_pos):
            if j == k:
                result = idx
    elif k in last_pos:
        for idx,j in enumerate(last_pos):
            if j == k:
                result = (idx+num)
    else:
        result = -1

    return result

# Driver Code
n = 6
arr=[1,2,3,4,5,6]
k = 6
result = binary_Search(arr,n,k)
print(result)