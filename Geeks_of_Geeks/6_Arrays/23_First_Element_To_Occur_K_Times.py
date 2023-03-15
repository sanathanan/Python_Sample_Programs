"""
First Element to occur K Times

Given an array of N integers. Find the first element that occurs at least K number of times.
"""
def firstElementKTime(arr,n,k):

    lst = []
    for i in arr:
        count = 0
        for idx, j in enumerate(arr):
            if i == j:
                count += 1
            if count == k:
                lst.append(i)
                break

    print(lst)

    # Checking count of each element in a lst
    dict={}
    for i in lst:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] +=1
    print(dict)

    new_lst=[]
    for key, val in dict.items():
        if val >= k:
            new_lst.append(key)
        else:
            continue

    print(new_lst)

    if len(new_lst) == 0:
        res = -1
    elif len(new_lst) == 1:
        res = new_lst
    else:
        len_ = len(new_lst)//2
        #len_ = len_ = len(lst)//2
        res = lst[len_]

    return res



# Driver Code
# n = 7
# k = 2
# arr=[1,7,4,3,6,4,7]

# n = 6
# k = 2
# arr=[3,4,1,3,4,4]

# n = 7
# k = 2
# arr=[1,7,4,3,4,4,7]

# n = 7
# k = 2
# arr=[1,7,4,3,4,8,7]

n = 10
k = 3
arr=[4,2,2,2,3,4,4,4,3,2]


result = firstElementKTime(arr,n,k)
print(result)