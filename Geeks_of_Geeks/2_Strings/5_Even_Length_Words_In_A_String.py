"""
In a given string. Printing all the even length strings.

Input : "This is a python language"
Output: This is python language
"""

# Method 1
input_1 = 'This is a python language'
lst_input_1 = input_1.split()
print("---------Method 1 ---------------")
print("Input String: ", lst_input_1)

for i in lst_input_1:
    if len(i)%2 == 0:
        print(i, end= ' ')

# Method 2
input_2 = 'This is a python language'
lst_input_2 = input_2.split()
print('\n',"---------Method 2 ---------------")
print("Input String: ", lst_input_2)

result = [i for i in lst_input_2 if len(i)%2 == 0]
print(result)

# Method 3
input_3 = 'Geek O Geeks'
lst_input_3 = input_3.split()
print("---------Method 3 ---------------")
print("Input String: ", lst_input_3)

result_2 = [x for i,x in enumerate(lst_input_3) if len(x)%2 == 0]
print(result_2)