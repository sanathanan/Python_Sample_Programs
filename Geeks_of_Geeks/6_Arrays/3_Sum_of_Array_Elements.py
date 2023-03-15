"""
Given an integer array arr of size n, you need to sum the elements of arr.

Example:
Input:
n = 3
arr[] = {3 2 1}
Output: 6
"""
# Method 1
def sumElement(arr):

    result = sum(arr)
    return result


# Driver Code
arr = [1,2,3]
result = sumElement(arr)
print(result)