"""
Method -1
"""
def swap1(input_lst_1, pos_1, pos_2):

    input_lst_1[0], input_lst_1[4] = input_lst_1[pos_2-1], input_lst_1[pos_1-1]

    return input_lst_1

"""
Method 2
"""
def swap2(input_lst_2, pos_1, pos_2):

    temp = input_lst_2[pos_1-1]
    input_lst_2[pos_1-1] = input_lst_2[pos_2-1]
    input_lst_2[pos_2-1] = temp

    return input_lst_2

"""
Method 3
"""
def swap3(input_lst_3, pos_1, pos_2):

    get = input_lst_3[pos_1-1], input_lst_3[pos_2-1]
    input_lst_3[pos_2 - 1], input_lst_3[pos_1-1] = get

    return input_lst_3

# Driver Code
input_lst_1=[10,20,30,40,50]
input_lst_2=[10,20,30,40,50]
input_lst_3=[10,20,30,40,50]
pos_1= 1
pos_2= 5

print("------------Method 1 ---------------")
print("Given List: ", input_lst_1)
print("Swapped List: ", swap1(input_lst_1, pos_1,pos_2))

print("------------Method 2 ---------------")
print("Given List: ", input_lst_2)
print("Swapped List: ", swap2(input_lst_2, pos_1, pos_2))

print("------------Method 3 ---------------")
print("Given List: ", input_lst_3)
print("Swapped List: ", swap3(input_lst_3, pos_1, pos_2))




