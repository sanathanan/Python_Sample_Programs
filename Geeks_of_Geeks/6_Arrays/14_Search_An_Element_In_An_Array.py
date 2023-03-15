"""
Search an element in an array

Given an integer array and another integer element. The task is to find if the given element is present in array or not.

The task is to complete the function search() which takes the array arr[], its size N and the element X
as inputs and returns the index of first occurrence of X in the given array. If the element X does not exist
in the array, the function should return -1.

Example:
Input:
n = 4
arr[] = {1,2,3,4}
x = 3
Output: 2
Explanation: There is one test case with array as {1, 2, 3 4} and element to be searched as 3.
Since 3 is present at index 2, output is 2.
"""
def search(arr,n, x):

    if x in arr:
        for idx,i in enumerate(arr):
            if i != x:
                pass
            else:
                return idx
    else:
        return -1




# Driver Code
n=4
arr=[1,2,3,4]
x=1
result= search(arr,n,x)
print(result)