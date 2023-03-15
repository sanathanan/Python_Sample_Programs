"""
Finding Index

Given an unsorted array Arr[] of N integers and a Key which is present in this array.
You need to write a program to find the start index( index where the element is first found from left in the array )
and end index( index where the element is first found from right in the array ).If the key does not exist in the
array then return -1 for both start and end index in this case.

Example:
Input:
N = 6
arr[] = { 1, 2, 3, 4, 5, 5 }
Key = 5
Output:  4 5
Explanation:
5 appears first time at index 4 and appears last time at index 5.(0 based indexing)
"""
def findIndex(arr,n,key):

    first_idx = ''
    for idx, i in enumerate(arr):
        if i == key:
            first_idx = str(idx)
            break
        else:
            first_idx = -1

    last_idx = ''
    for idx,i in reversed(list(enumerate(arr))):
        if i == key:
            last_idx = str(idx)
            break
        else:
            last_idx = -1



    return first_idx, last_idx
# Driver Code
n= 6
# arr=[1,2,3,4,5,5]
arr=[6, 5, 4, 3, 1, 2]
key=4
result1, result2 = findIndex(arr,n,key)
print(result1, result2)