"""
Check if a string starts with a substring

Given a string str, the task is to check if a string starts with a given substring or not using regular expression

Example:
Input: String: "geeks for geeks makes learning fun"
       Substring: "geeks"
Output: True
"""

# Method 1
import re
print("------Method 1 ---------")
str_1 = "geekss for geeks makes learning fun"
subString = 'geeks '

if subString in str_1:
    x = re.compile('^'+subString)
    match = re.search(x, str_1)

    if match:
        print("The substring is started with a given string")
    else:
        print("The substring is not started with a given string")

else:
    print("The substring is not present in the given string")

# Method 2
import re
print("------Method 2 ---------")
str_2 = "geeks for geeks makes learning fun"
subString_2 = 'geeks '

if subString_2 in str_2:
    x = re.compile('\A'+subString_2)
    match = re.search(x, str_2)

    if match:
        print("The substring is started with a given string")
    else:
        print("The substring is not started with a given string")

else:
    print("The substring is not present in the given string")