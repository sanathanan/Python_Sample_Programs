"""
Finding all numbers in a string

Example:
Input: abcd11gdf15hnnn678hh4
Output: 11 15 678 4

Input: 1abcd133hhe0
Output: 1 133 0
"""
import re

def numbers_Check(str):

    pattern = re.compile('[0-9]+')
    result = re.findall(pattern,str)
    return result


def main():
    print(numbers_Check('abcd11gdf15hnnn678hh4'))
    print(numbers_Check('1abcd133hhe0'))

main()