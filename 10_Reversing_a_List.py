# Reversing a List
"""
Method 1
"""
def rev_lst_1(lst_1):
    res = lst_1.reverse()
    return res


"""
Method 2
"""
def rev_lst_2(lst_2):
    l=[]
    for i in lst_2:
        l.insert(0,i)
    return l

"""
Method 3
"""
def rev_lst_3(lst_3):
    l=[]
    l = lst_3[::-1]
    return l

"""
Method 4
"""
def rev_lst_4(lst_4):
    res = reversed(lst_4)
    return list(res)


# Driver Code
lst_1=[1,2,3,4,5,6,7,8,9,10]
lst_2=[1,2,3,4,5,6,7,8,9,10]
lst_3=[1,2,3,4,5,6,7,8,9,10]
lst_4=[1,2,3,4,5,6,7,8,9,10]


print("------------Method 1 ---------------")
print("Given List: ",lst_1)
print("Reversed List: ", rev_lst_1(lst_1))

print("------------Method 2 ---------------")
print("Given List: ",lst_2)
print("Reversed List: ", rev_lst_2(lst_2))

print("------------Method 3 ---------------")
print("Given List: ",lst_3)
print("Reversed List: ", rev_lst_3(lst_3))

print("------------Method 4 ---------------")
print("Given List: ",lst_4)
print("Reversed List: ", rev_lst_4(lst_4))
