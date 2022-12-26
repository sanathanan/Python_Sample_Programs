

"""
Method 1
"""
def swap1(input_lst):
    res = len(input_lst)
    return res

"""
Method 2
"""
def swap2(input_lst):
    counter = 0
    for i in input_lst:
        counter += 1
    return counter



# Driver Code
input_lst = [10,20,30,40,50]


print("------------Method 1 ---------------")
print("Given List: ", input_lst)
print("Swapped List: ", swap1(input_lst))

print("------------Method 2 ---------------")
print("Given List: ", input_lst)
print("Swapped List: ", swap2(input_lst))

