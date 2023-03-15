"""
Printing alternate elements in a array

You are given an array A of size N. You need to print elements of A in alternate order (starting from index 0).

Example:
Input:
N = 4
A[] = {1, 2, 3, 4}
Output:
1 3
"""
def printAl(arr,n):

    dict={}
    for idx,i in enumerate(arr):
        dict[idx+1] = i

    lst= []
    for i,j in dict.items():
        if i%2 != 0:
          lst.append(j)
        else:
            pass

    str_ = ''
    for i in lst:
        str_ += (''.join(str(i)) + ' ')

    return str_


def printAl_1(arr,n):

    str_ = ''
    for i in range(0,n,2):
        str_ += (str(arr[i]) + ' ')

    return str_

# Driver Code
n = 5
arr = [1,2,3,4, 5]
result = printAl(arr,n)
print(result)

result_1 = printAl_1(arr,n)
print(result_1)
