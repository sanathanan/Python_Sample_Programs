"""
Check String Contains Defined Characters

Example:
Input: ‘657’
let us say regular expression contain following characters-(‘78653’)
Output: Valid
"""
# Method 1
import re
print("-----Method 1 ---------")
input_1 = '657'
exp ='78653'


# ^[78653]+$
# ^ - Starts with
# [] - set of Characeters
# + - one or more occurances
# $ - Ends with
pattern = re.compile('^[78653]+$')

result = re.search(pattern,input_1)
try:
    if result.span():
        print("Valid String")
except:
    print("No Valid String")

# print(result.span())

# if re.search(pattern,input_1):
#     print("Valid String")
# else:
#     print("Invalid String")