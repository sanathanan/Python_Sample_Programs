"""
Method 1
"""
def max1(a,b):
    if a >= b:
        return a
    elif a<b:
        return b


# Driver Code
a = 10
b = 20

print("------------Method 1 ---------------")
print("Given Numbers: ", a, " ", b)
print("Maximum Number: ", max1(a,b))

print("------------Method 2 ---------------")
print("Given Numbers: ", a, " ", b)
print("Maximum Number: ", max(a,b))

print("------------Method 3 ---------------")
print("Given Numbers: ", a, " ", b)
print("Maximum Number: ", (a if a>= b else b ))

print("------------Method 4 ---------------")
print("Given Numbers: ", a, " ", b)
print("Maximum Number: ", f'{(lambda a,b : a if a>=b else b)}')

