"""
Finding Length of a String
"""
# Method 1
str_1 = 'Hello How are you'
len_1 = len(str_1)
print("---------Method 1 ------------")
print("The Length of the String: ", len_1)

# Method 2
str_2 = 'Hello How are you'

counter = 0
for i in str_2:
    counter += 1
print("---------Method 2 ------------")
print("The Length of the String: ", counter)

# Method 3
str_3 = 'Hello How are you'

result = sum([1 for i in str_3])
print("---------Method 3 ------------")
print("The Length of the String: ", result)

# Method 4
str_4 = 'Hello How are you'
count = 0
for i,j in enumerate(str_4):
    count = count + 1
print("---------Method 4 ------------")
print("The Length of the String: ", count)
