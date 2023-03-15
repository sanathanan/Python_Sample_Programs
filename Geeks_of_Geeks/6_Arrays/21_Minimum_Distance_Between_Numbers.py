"""
Minimum distance between 2 numbers
You are given an array A, of N elements. Find minimum index based distance between two elements of the array,
x and y such that (x!=y).

Complete the function minDist() which takes the array, n, x and y as input parameters and returns the minimum
distance between x and y in the array. If no such distance is possible then return -1.

Example:
Input:
N = 4
A[] = {1,2,3,2}
x = 1, y = 2
Output: 1
Explanation: x = 1 and y = 2. There are two distances between x and y, which are
1 and 3 out of which the least is 1.
"""

def minDist(arr,n,x,y):

    if x==y:
        return -1

    if x not in arr:
        return -1

    if y not in arr:
        return -1

    if x and y in arr:
        lst_x = []
        lst_y = []
        for idx, i in enumerate(arr):
            if i == x:
                lst_x.append(idx+1)
            if i == y:
                lst_y.append(idx+1)

        # print(lst_x)
        # print(lst_y)

        if len(lst_x)>1:
            index_x = max(lst_x)
            index_y = max(lst_y)
            # print(index_x)
            # print(index_y)
            if index_x > index_y:
                count1 = index_x - index_y
            else:
                count1 = index_y - index_x

            index_x2 = min(lst_x)
            index_y2 = max(lst_y)
            # print(index_x)
            # print(index_y)
            if index_x2 > index_y2:
                count2 = index_x2 - index_y2
            else:
                count2 = index_y2 - index_x2

        if len(lst_y)>1:
            index_x = max(lst_x)
            index_y = max(lst_y)
            # print(index_x)
            # print(index_y)
            if index_x > index_y:
                count1 = index_x - index_y
            else:
                count1 = index_y - index_x

            index_x2 = max(lst_x)
            index_y2= min(lst_y)
            # print(index_x)
            # print(index_y)
            if index_x2 > index_y2:
                count2 = index_x2 - index_y2
            else:
                count2 = index_y2 - index_x2

        if len(lst_x) == len(lst_y):
            index_x = max(lst_x)
            index_y = max(lst_y)
            # print(index_x)
            # print(index_y)
            if index_x > index_y:
                count1 = index_x - index_y
            else:
                count1 = index_y - index_x

            index_x2 = max(lst_x)
            index_y2 = max(lst_y)
            # print(index_x)
            # print(index_y)
            if index_x2 > index_y2:
                count2 = index_x2 - index_y2
            else:
                count2 = index_y2 - index_x2

    if count1<count2:
        return count1
    else:
        return count2



# Driver Code
# n= 4 # ans: 1
# arr= [1,2,3,2]
# x=1
# y=2

# n=83 # ans:34
# arr= [98,78,10,12,59,37,45,18,1,56,37,14,3,32,85,10,69,89,29,93,44,16,26,13,50,75,79,21,20,33,55,17,63,64,80,21,
#       52,24,90,52,80,26,18,34,57,2,95,25,42,23,17,85,39,94,50,40,21,28,12,40,61,67,9,23,30,88,95,34,64,85,85,95,
#       62,54,28,19,55,22,95,49,97,64,33]
# x=34
# y=56


# n= 62 # ans: 13
# arr = [96,82,48,76,34,19,7,80,36,57,77,34,19,35,5,57,16,66,42,62,89,19,60,19,25,16,20,51,77,75,12,73,8,11,
#        100,93,81,58,72,17,14,48,2,33,82,6,41,49,72,34,10,12,53,21,30,77,36,49,79,13,75,42]
# x= 36
# y= 33

n= 92 # ans: 33
arr= [52,60,40,8,14,90,63,53,48,41,7,33,80,82,82,27,82,81,48,91,63,37,63,32,6,44,52,80,81,60,71,84,71,62,92,84,51,6,88,98,
      46,94,83,26,27,64,4,60,96,51,2,11,87,64,94,93,60,45,24,92,56,46,76,78,7,19,13,10,24,100,59,21,45,93,98,23,9,1,34,4,51,
      35,14,38,51,7,82,10,4,57,1,11]
x=1
y=27
result= minDist(arr,n,x,y)
print(result)


