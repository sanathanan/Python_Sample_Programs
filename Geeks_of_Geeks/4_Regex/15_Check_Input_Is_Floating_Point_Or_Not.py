"""
Check whether the input is Floating point number or not

Example:
Input:  1.20
Output: Floating point number

Input: -3
Output: Not a Floating point number
"""
import re

def floating_Check(str):

    pattern = re.compile(r'[+-]?[0-9]+\.[0-9]+')
    result = re.search(pattern, str)

    if result:
        return "Floating Point Number"
    else:
        return "Not a Floating Point Number"

def main():
    print(floating_Check("1.20"))
    print(floating_Check('-3'))
    print(floating_Check('abcd'))

main()