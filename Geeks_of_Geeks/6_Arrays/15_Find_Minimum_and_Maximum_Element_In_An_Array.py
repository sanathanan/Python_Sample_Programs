"""
Finding Minimum and Maximum Element in an array

Example:
Input:
N = 6
A[] = {3, 2, 1, 56, 10000, 167}
Output:
min = 1, max =  10000
"""

def getMinMax(arr,n):
    min_ = min(arr)
    max_ = max(arr)

    return min_, max_

# Driver Code
n = 6
arr = [3,2,1,56,10000,167]
result1, result2 = getMinMax(arr,n)
print(result1, result2)
