"""
Accept String Starting With Vowel

Example:
Input: animal
Output: Accepted

Input: zebra
Output: Not Accepted
"""
import re

def vowel_Check(str):

    pattern = re.compile(r'^(a|e|i|o|u|A|E|I|O|U)([a-zA-Z0-9]*)')
    result = re.search(pattern, str)

    if result:
        return "Valid"
    else:
        return "Non Valid"

def main():
    print(vowel_Check("animal"))
    print(vowel_Check("zebra"))

main()

