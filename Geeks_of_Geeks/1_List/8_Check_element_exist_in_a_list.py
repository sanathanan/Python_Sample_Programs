# To check element exist in a list


"""
Method 1
"""
def check_1(lst_1, user_input):
    c = ''
    for i in lst_1:
        if i == user_input:
            c = "Number exists"
    if len(c) == 0:
        c = "Number not found"
    return c



# Driver Code
lst_1 =[1,2,4,67,89,90]
user_input = int(input("Enter the number to check: "))


print("------------Method 1 ---------------")
print("Given List: ", lst_1)
print("Given Element exist or not: ", check_1(lst_1, user_input))

print("------------Method 2 ---------------")
print("Given List: ", lst_1)
if user_input in lst_1:
    c = 'Number found'
    print("Given Element exist or not: ", c)
else:
    c = "Number not found"
    print("Given Element exist or not: ", c)

print("------------Method 2 ---------------")
print("Given List: ", lst_1)
exist_count = lst_1.count(user_input)
if exist_count > 0:
    c = 'Number found'
    print("Given Element exist or not: ", c)
else:
    c = "Number not found"
    print("Given Element exist or not: ", c)