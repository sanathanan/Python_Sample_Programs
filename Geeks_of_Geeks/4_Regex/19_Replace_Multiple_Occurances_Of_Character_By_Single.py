"""
Replace Multiple Occurances of Characters by single

Example:
Input : Geeksforgeeks, ch = 'e'
Output : Geksforgeks
"""
import re
print("--------Method 1 ---------")

def occurance_Check(str, ch):

    pattern = ch+'{2,}' # Checking the specified character is occurring more than 1 time. Then replace that string with
                        #
    replace = ch
    result = re.sub(pattern, replace, str)
    return result

def main():
    print(occurance_Check("Geeksforgeeks",ch='e'))
    print(occurance_Check("Wiiiin", ch='i'))


main()