"""
Reverse Array in Group

Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.

Note: If at any instance, there are no more subarrays of size greater than or equal to K,
then reverse the last subarray (irrespective of its size). You shouldn't return any array, modify the given array in-place.

Example:
Input: N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
"""

def reverseInGroups(arr,n,k):

    first_pos = arr[:k]
    last_pos = arr[k:]

    first_pos_ = first_pos[::-1]
    last_pos_ = last_pos[::-1]

    result = (first_pos_ + last_pos_)

    result_ = ' '.join(map(str,result))

    return result_

# Driver Code
n=4
k=3
arr=[5,6,8,9]
result = reverseInGroups(arr,n,k)
print(result)