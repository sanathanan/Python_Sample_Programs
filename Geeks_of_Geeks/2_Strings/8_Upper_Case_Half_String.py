"""
Given a String, perform uppercase of later part of string.

    Input : test_str = ‘geeksforgeek'.

    Output : geeksfORGEEK

    Explanation : Latter half of string is uppercased.

"""
# Method 1
print('-------------Method 1 -------------------')
input_1 = 'geeksforgeek'

str_len = len(input_1)
str_len_half = len(input_1)//2

result = ''
if str_len %2 == 0:
    first_half = input_1[:str_len_half]
    second_half = (input_1[str_len_half:]).upper()
    result = first_half + second_half
    print(result)
else:
    first_half = input_1[:str_len_half]
    second_half = (input_1[str_len_half:]).upper()
    result = first_half + second_half
    print(result)

# Method 2
print('-------------Method 2 -------------------')
input_2 = 'geeksforgeek'
half_2 = len(input_2)//2

# Slicing Technique
result = input_2[:half_2] + input_2[half_2:].upper()
print(result)

# Method 3
print('-------------Method 3 -------------------')
input_3 = 'geeksforgeek'
half_3 = len(input_2)//2

result_3 = ''
# For loop
for i,x in enumerate(input_3):
    if i > half_3:
        result_3 += input_3[i].upper()
    else:
        result_3 += input_3[i]
print(result_3)

# Method 4
print('-------------Method 4 -------------------')
input_4 = 'geeksforgeek'
half_4 = len(input_2)//2

result_4 = ''
# For loop
for i,x in enumerate(input_4):
    if i > half_4:
        result_4 += x.upper()
    else:
        result_4 += x
print(result_4)
