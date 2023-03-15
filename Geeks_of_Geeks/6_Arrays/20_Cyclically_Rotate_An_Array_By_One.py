"""
Cyclically Rotate an array by one

Given an array, rotate the array by one position in clock-wise direction.

Example:
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output: 5 1 2 3 4
"""

def rotate(arr,n):
    len_ = len(arr)
    first_pos = arr[len_-1]
    last_pos = arr[:len_-1]

    result = str(first_pos) + ' ' + ' '.join(map(str,last_pos))

    return result

# Driver Codes
n=8
arr=[9, 8, 7, 6, 4, 2, 1, 3]
result = rotate(arr,n)
print(result)