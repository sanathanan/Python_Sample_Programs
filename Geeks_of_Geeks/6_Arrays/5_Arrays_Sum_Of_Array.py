"""
Arrays (Sum of Array)

Given an array of N integers. Your task is to print the sum of all of the integers.

Example:
Input:
4
1 2 3 4
Output:
10
"""

def getSum(arr,n):

    result = sum(arr)

    return result


# Driver Code
n=4
arr = [1,2,3,4]
result = getSum(arr,n)
print(result)