"""
Method 1
"""
def swap1(input_lst):
    lst =[]
    for i in input_lst:
        c = i[1], i[0]
        lst.append(c)
    return lst


# Driver Code
input_lst =[(2,3),(3,4),(5,6)]

print("------------Method 1 ---------------")
print("Given List: ", input_lst)
print("Swapped List: ", swap1(input_lst))


