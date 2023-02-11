"""
Given a string. The task is to count the number of Uppercase, Lowercase, special character and numeric values present
in the string using Regular expression in Python.

Example:
Input :
"ThisIsGeeksforGeeks!, 123"

Output :
No. of uppercase characters = 4
No. of lowercase characters = 15
No. of numerical characters = 3
No. of special characters = 2
"""
# Method 1
import re

print("-----------Method 1 -----------")
str_1 = 'ThisIsGeeksforGeeks!, 123'

upper_Case = re.findall(r'[A-Z]',str_1)
lower_Case = re.findall(r'[a-z]', str_1)
numeric = re.findall(r'[0-9]', str_1)
special_Charac = re.findall(r'[!,.]', str_1)


print("No.Of Upper_Case Character is: {} = {}".format(upper_Case, len(upper_Case)))
print("No.Of Lower_Case Character is: {} = {}".format(lower_Case, len(lower_Case)))
print("No.Of Numeric Character is: {} = {}".format(numeric, len(numeric)))
print("No.Of Special Character is: {} = {}".format(special_Charac, len(special_Charac)))