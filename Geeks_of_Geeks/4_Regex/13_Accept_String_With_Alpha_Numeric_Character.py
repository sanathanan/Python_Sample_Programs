"""
Accept String with alphanumeric character

Example:
Input: ankitrai326
Output: Accept

Input: ankirai@
Output: Discard
"""
import re

def alpha_Numeric_Check(str):

    pattern = re.compile(r'([A-Za-z0-9]+$)')
    result = re.search(pattern, str)

    if result:
        return "Valid"
    else:
        return "Non Valid"

def main():
    print(alpha_Numeric_Check("ankitrai326"))
    print(alpha_Numeric_Check("ankirai@"))
    print(alpha_Numeric_Check("geeksforgeeks"))
    print(alpha_Numeric_Check("ankit."))

main()

