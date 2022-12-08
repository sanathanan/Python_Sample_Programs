"""
Swapping "i"th element with "j"th element in a list
"""
"""
Method 1
"""
def swap1(input_lst, i , j):

    for k in range(len(input_lst)):
        if input_lst[k] == i:
            input_lst[k] = j
        elif input_lst[k] == j:
            input_lst[k] = i
    return input_lst


# Driver Code
input_lst =[4, 7, 8, 0, 8, 4, 2, 9, 4, 8, 4]
i = 4
j = 8


print("------------Method 1 ---------------")
print("Given List: ", input_lst)
print("Swapped List: ", swap1(input_lst,i, j))
