"""
Finding First and Last occurrences of X

Given a sorted array arr containing n elements with possibly duplicate elements,
the task is to find indexes of first and last occurrences of an element x in the given array.

Example:
Input:
n=9, x=5
arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
Output:  2 5
Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5.

Note: If the number x is not found in the array just return both index as -1.
"""

def find(arr,n,x):

    lst = []
    if x in arr:
        for idx, i in enumerate(arr):
            if i == x:
                lst.append(idx)
        return lst[0], lst[-1]
    else:
        return -1, -1






# Driver Code
n = 9
arr=[1, 3, 5, 5, 5, 5, 67, 123, 125]
x = 68
result1, result2 = find(arr,n,x)
print(result1, result2)
