"""
Method 1:
"""
def swapping1(input_List_1):
    temp = input_List_1[0]
    input_List_1[0] = input_List_1[-1]
    input_List_1[-1] = temp
    return input_List_1

"""
Method 2
"""
def swapping2(input_List_2):
    input_List_2[0], input_List_2[-1] = input_List_2[-1], input_List_2[0]
    return input_List_2


"""
Method 3
"""
def swapping3(input_List_3):
    first_element = input_List_3[0]
    last_element = input_List_3[-1]
    input_List_3[0] = last_element
    input_List_3[-1] = first_element
    return input_List_3

"""
Method 4
"""
def swapping4(input_List_4):
    get = input_List_4[0], input_List_4[-1]
    input_List_4[-1], input_List_4[0] = get
    return input_List_4


# Driver Code
input_List_1=[24,56,78,85,54]
input_List_2=[24,56,78,85,54]
input_List_3=[24,56,78,85,54]
input_List_4=[24,56,78,85,54]

print("------------Method 1---------------")
print("Given List: ", input_List_1)
print("Swapped List: ", swapping1(input_List_1))

print("------------Method 2---------------")
print("Given List: ", input_List_2)
print("Swapped List: ", swapping2(input_List_2))

print("------------Method 3---------------")
print("Given List: ", input_List_3)
print("Swapped List: ", swapping3(input_List_3))

print("------------Method 4---------------")
print("Given List: ", input_List_4)
print("Swapped List: ", swapping4(input_List_4))
