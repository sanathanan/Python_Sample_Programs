"""
Most occurring number in  a string
Example:
Input :geek55of55geeks4abc3dr2
Output :55

Input :abcd1def2high2bnasvd3vjhd44
Output :2
"""
import re
from collections import Counter

def most_Occuring_Number(str):

    pattern = re.compile('[0-9]+')
    result = re.findall(pattern, str)
    print(result)

    dict_ = dict(Counter(result))
    print(dict_)

    for i,j in dict_.items():
        if j >1:
            return i



def main():
    print(most_Occuring_Number('geek55of55geeks4abc3dr2'))
    print(most_Occuring_Number('abcd1def2high2bnasvd3vjhd44'))

main()