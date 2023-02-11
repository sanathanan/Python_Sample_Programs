"""
Check whether a string starts and ends with the same character or not (using Regular Expression)

Example:

Input :abba
Output :Valid

Input :a
Output :Valid
"""

# Method 1
import re

str1 = 'abba'
# ^[a-z]$ - Starts with and ends with a to z
# | - To combine 2 regex commands
# ^([a-z]).*\1$ - Starts with and ends witt a to z any character with Zero or more occurances and \1 will check first character repeats
# another time.
result_1 = re.search(r'^[a-z]$|^([a-z]).*\1$',str1)

if result_1:
    print("Valid")
else:
    print("Not Valid")
