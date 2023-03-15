"""
Count of Smaller Elements

Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.

Example:
nput:
N = 6
A[] = {1, 2, 4, 5, 8, 9, 10}
X = 9
Output:
5
"""
def count_Of_Elements(arr,n,x):

    count = 0
    for i in (arr):
        if i <= x:
            count += 1
        else:
            pass

    return count

# Driver Code
n = 6
arr=[1,2,4,5,8,9,10]
x = 9
result = count_Of_Elements(arr,n,x)
print(result)