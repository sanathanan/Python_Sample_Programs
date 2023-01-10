"""
Given a string in Python. The task is to check whether the string has at least one letter(character) and one number.
Return “True” if the given string fully fill the above condition else return “False” (without quotes).

Examples:

Input: welcome2ourcountry34
Output: True

Input: stringwithoutnum
Output: False
"""

# Method 1
print('------------Method 1-----------------')

def str_test(input_1):
    flag_l = False
    flag_n = False

    for i in input_1:
        if i.isalpha():
            flag_l = True

        if i.isdigit():
            flag_n = True

    return flag_l and flag_n


input_1 = 'welcome2ourcountry34'
print(str_test(input_1))

